#!/usr/bin/env python3
# Copy of vsenthil7/ai-tool-support-kb scripts/turn_close/turn_close.py (master copy). Change it there first, then copy here.
"""One command that closes a turn (Git Turn Protocol v1.2). [claude, T057]

Run from the repo root, after the turn record is written:
  python3 -I scripts/turn_close/turn_close.py --turn T057 --topic "turn-close script" --ai claude \
      --research "..." --gaps "none" [--session-log X.jsonl] [--record turns/...md] \
      [--summary "timeline text"] [--trailer "Co-Authored-By: ..."]...

Steps (in this order):
 1. git pull --rebase --autostash origin main; fill `- Read at:` if the record has none.
 2. P1 check (§2b): if the T number is already on origin/main, rename the record + its title/Turn lines
    to the next free number. Only unpushed files are renamed.
 3. Measure usage: scripts/usage_session.py -> usage/YYYY/MM/DD/<project>_<ai>_usage_session-<id>_<stamp>.csv;
    fill the record's `## USAGE` section with this turn's row.
 4. Append the record's line to index/timeline.md if missing.
 5. Stage only the files this turn changed; secret_scan.py on them; stop on any hit.
 6. One commit: `turn(<ai>): T### <topic>` + trailers.
 7. Push. If rejected: undo the local (unpushed) commit, pull again, redo 2-6. Up to 3 tries. Never forces a push.
 8. Check `git ls-remote origin main` == local head.
 9. Print the Git Evidence block.

Rules: never deletes files or branches, never rewrites pushed history, never edits other pages' lines.
Per-repo settings: optional `.turn_close.json` (keys in DEFAULTS) for repos with other names/folders.
Exit codes: 0 done, 2 secret hit, 3 push failed after 3 tries, 4 verify failed, 5 merge conflict (left for a human).
"""
import argparse, csv, datetime as dt, glob, os, re, subprocess, sys
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/London")
# Per-repo settings: optional `.turn_close.json` at the repo root overrides these (T064).
DEFAULTS = {
    "records_root": "turns",                        # folder that holds turn records
    "record_glob": "turns/*/*/*/{turn}-*.md",        # where this turn's record lives
    "prefix": "T",                                   # turn id = prefix + zero-padded number
    "width": 3,
    "timeline": "index/timeline.md",
    "timeline_format": "- {when} — {turn} [{ai}, {turn}] — {summary} — `{rec}`",
    "usage_dir": "usage/{Y}/{m}/{d}",
    "usage_script": "scripts/usage_session.py",
    "secret_scan": "scripts/secret_scan.py",
    "commit_format": "turn({ai}): {turn} {topic}",
    "project": "",                                   # short name in usage file names (default: repo name)
    "timeline_day_heading": "",                      # e.g. "## {date}": added once per day before the line
    "timeline_footer": "",                           # a last line that must stay last (line goes above it)
}
CFG = dict(DEFAULTS)
TIMELINE = CFG["timeline"]


def load_cfg():
    global TIMELINE
    if os.path.exists(".turn_close.json"):
        import json
        with open(".turn_close.json", encoding="utf-8") as f:
            extra = json.load(f)
        unknown = set(extra) - set(DEFAULTS)
        if unknown:
            raise Stop(5, f".turn_close.json has unknown keys: {sorted(unknown)}")
        CFG.update(extra)
    TIMELINE = CFG["timeline"]
    global PROJECT
    if CFG["project"]:
        PROJECT = CFG["project"]
HOOK = "TURN_CLOSE_TEST_BEFORE_PUSH"  # tests only: a command run once before the first push


class Stop(Exception):
    def __init__(self, code, msg):
        super().__init__(msg); self.code = code


def git(*a, check=True):
    r = subprocess.run(["git", *a], capture_output=True, text=True)
    if check and r.returncode:
        raise Stop(5, f"git {' '.join(a)} failed:\n{r.stdout}{r.stderr}")
    return r


def out(*a):
    return git(*a).stdout.strip()


def log(msg):
    print(f"[turn_close] {msg}", file=sys.stderr)


# ---------- record helpers ----------
def tnum(t):
    return int(re.search(r"(\d+)$", t).group(1))


def find_record(turn, given):
    if given:
        return given
    hits = sorted(glob.glob(CFG["record_glob"].format(turn=turn)))
    dirty = set(changed_files())
    mine = [h for h in hits if h in dirty] or hits
    if len(mine) != 1:
        raise Stop(5, f"cannot pick the record for {turn}: {mine or 'none found'} (use --record)")
    return mine[0]


def changed_files():
    """Files changed or new in the working tree (tracked + untracked), not ignored."""
    res = []
    for line in git("status", "--porcelain", "-uall").stdout.splitlines():
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ")[1]
        res.append(path.strip('"'))
    return res


def turns_on_remote():
    names = out("ls-tree", "-r", "--name-only", "origin/main", CFG["records_root"]).splitlines()
    nums = {}
    idre = re.compile(rf"^({re.escape(CFG['prefix'])}\d+)-")
    for n in names:
        m = idre.match(os.path.basename(n))
        if m:
            nums.setdefault(m.group(1), []).append(n)
    return nums


def p1_check(rec, turn):
    """Rename the (unpushed) record if its T number is taken on origin/main. Returns (rec, turn)."""
    remote = turns_on_remote()
    taken = [p for p in remote.get(turn, []) if p != rec]
    if not taken:
        return rec, turn
    new = f"{CFG['prefix']}{max(tnum(t) for t in remote) + 1:0{CFG['width']}d}"
    if out("ls-tree", "--name-only", "origin/main", rec):
        raise Stop(5, f"{rec} is already pushed; refusing to rename it")
    newrec = os.path.join(os.path.dirname(rec), os.path.basename(rec).replace(f"{turn}-", f"{new}-", 1))
    s = open(rec, encoding="utf-8").read()
    s = re.sub(rf"^# {turn}\b", f"# {new}", s, count=1, flags=re.M)
    s = re.sub(rf"^(- Turn: ){turn}\b", rf"\g<1>{new}", s, flags=re.M)
    open(newrec, "w", encoding="utf-8").write(s)
    os.remove(rec)  # our own unpushed file, moved (not a delete of history)
    log(f"P1: {turn} is taken on origin/main by {taken[0]} -> renamed to {new} ({newrec})")
    return newrec, new


def fill_read_at(rec, head):
    s = open(rec, encoding="utf-8").read()
    m = re.search(r"^- Read at:[ \t]*(\S*)", s, re.M)
    if m and m.group(1) and m.group(1) not in ("?", "<READ-AT>", "TBD"):
        return m.group(1)
    if m:
        s = s[:m.start()] + f"- Read at: {head}" + s[m.end():]
    else:
        s = re.sub(r"^(## Metadata\n)", rf"\g<1>- Read at: {head}\n", s, count=1, flags=re.M)
    open(rec, "w", encoding="utf-8").write(s)
    return head


def set_section(s, header_re, body):
    m = re.search(header_re, s, re.M)
    if not m:
        return s.rstrip("\n") + "\n\n" + body + "\n"
    nxt = re.search(r"^## ", s[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(s)
    return s[:m.start()] + body + "\n\n" + s[end:].lstrip("\n")


# ---------- usage ----------
def measure_usage(rec, ai, session_log, project, stamp):
    if not session_log or not os.path.isfile(session_log):
        body = ("## USAGE (UNAVAILABLE — no session log found)\n"
                "No session log on this surface. Gap noted in the Git Evidence block.")
        s = open(rec, encoding="utf-8").read()
        open(rec, "w", encoding="utf-8").write(set_section(s, r"^## USAGE\b.*$", body))
        return None, "UNAVAILABLE (no session log)"
    sid = os.path.basename(session_log).split(".")[0][:8]
    d = dt.datetime.now(TZ)
    udir = CFG["usage_dir"].format(Y=f"{d:%Y}", m=f"{d:%m}", d=f"{d:%d}")
    path = f"{udir}/{project}_{ai}_usage_session-{sid}_{stamp}.csv"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    r = subprocess.run([sys.executable, "-I", CFG["usage_script"], session_log, path],
                       capture_output=True, text=True)
    if r.returncode or not os.path.isfile(path):
        raise Stop(5, f"usage_session.py failed:\n{r.stderr}")
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    cur = rows[-1]
    n = lambda k, row=cur: f"{int(float(row[k])):,}"
    body = ["## USAGE (MEASURED — session log via `" + CFG["usage_script"] + "`, up to the commit)",
            "| model calls | input | cache read | cache write | output | effective units |",
            "|---|---|---|---|---|---|",
            f"| {cur['calls']} | {n('input')} | {n('cache_read')} | {n('cache_write')} | {n('output')} | {n('effective_units')} |",
            ""]
    if len(rows) > 1:
        p = rows[-2]
        body.append(f"Previous turn on this page, final (incl. after its commit): {p['calls']} calls · "
                    f"{n('effective_units', p)} effective units.")
    body.append(f"CSV: `{path}`. Usage after this commit goes into the next turn's record.")
    s = open(rec, encoding="utf-8").read()
    open(rec, "w", encoding="utf-8").write(set_section(s, r"^## USAGE\b.*$", "\n".join(body)))
    return path, f"{cur['calls']} calls · {n('effective_units')} effective units (MEASURED, to commit)"


# ---------- evidence ----------
def evidence(turn, read_at, commit, verified, usage, research, gaps):
    return "\n".join(["Git Evidence",
                      f"- Repo: {REPO} · main",
                      f"- Turn: {turn} · Read at: {read_at}",
                      f"- Commit: {commit}",
                      f"- Verified: {verified}",
                      f"- Usage: {usage}",
                      f"- Research: {research}",
                      f"- Gaps: {gaps}"])


def put_evidence(rec, block):
    """Write the block into the ASSISTANT RESPONSE fence: replace an existing block or <GIT-EVIDENCE>,
    else add it before the closing fence."""
    s = open(rec, encoding="utf-8").read()
    if "<GIT-EVIDENCE>" in s:
        s = s.replace("<GIT-EVIDENCE>", block)
    elif "Git Evidence\n- Repo:" in s:
        s = re.sub(r"Git Evidence\n(- [A-Za-z]+:.*\n?)+", block + "\n", s)
    else:
        m = re.search(r"^## ASSISTANT RESPONSE\s*\n+(`{3,})", s, re.M)
        if m:
            fence = m.group(1)
            close = s.find("\n" + fence, m.end())
            s = s[:close] + "\n\n" + block + s[close:] if close != -1 else s + "\n" + block + "\n"
        else:
            s = s.rstrip("\n") + "\n\n" + block + "\n"
    open(rec, "w", encoding="utf-8").write(s)


def timeline_line(rec, turn, ai, summary):
    s = open(rec, encoding="utf-8").read()
    m = re.search(r"^# \S+ — (\d{4}-\d\d-\d\d) (\d\d:\d\d)", s, re.M)
    date, time = (m.group(1), m.group(2)) if m else dt.datetime.now(TZ).strftime("%Y-%m-%d %H:%M").split()
    line = CFG["timeline_format"].format(when=f"{date} {time}", date=date, time=time, turn=turn, ai=ai,
                                         summary=summary, rec=rec)
    return line, date


def add_timeline(rec, line, date=None):
    s = open(TIMELINE, encoding="utf-8").read() if os.path.exists(TIMELINE) else "# Timeline\n"
    turn = re.search(r"([^/]+?)-\d{4}-", os.path.basename(rec) + "-0000-")
    tid = turn.group(1) if turn else ""
    # already there? (by file name, or by the turn tag for formats without a path, e.g. "[claude, T050]")
    if os.path.basename(rec) in s or line in s or (tid and re.search(rf"[\[ ,]{re.escape(tid)}\]", s)):
        return False
    foot = CFG["timeline_footer"]
    head = s.rstrip("\n")
    tail = ""
    if foot and head.endswith(foot):
        head, tail = head[: -len(foot)].rstrip("\n"), "\n\n" + foot
    add = line
    if CFG["timeline_day_heading"]:
        h = CFG["timeline_day_heading"].format(date=date or dt.datetime.now(TZ).strftime("%Y-%m-%d"))
        if not re.search(rf"^{re.escape(h)}$", s, re.M):
            add = "\n" + h + "\n" + line
    with open(TIMELINE, "w", encoding="utf-8") as f:
        f.write(head + "\n" + add + tail + "\n")
    return True


# ---------- main flow ----------
def sync(our_commit):
    """Bring origin/main in. If we hold an unpushed turn commit, undo it (soft) so the redo is one clean commit."""
    if our_commit and out("rev-parse", "HEAD") == our_commit:
        git("reset", "--soft", "HEAD~1")  # local, unpushed commit only
        git("restore", "--staged", ".")
        if os.path.exists(TIMELINE):  # our timeline line is re-added after the pull
            git("checkout", "--", TIMELINE)
    r = git("pull", "--rebase", "--autostash", "origin", "main", check=False)
    if r.returncode:
        raise Stop(5, f"pull failed — merge conflict left for a human, nothing overwritten:\n{r.stdout}{r.stderr}")
    git("fetch", "origin", "main")


def prepare(a, rec, turn, read_at, files, stamp):
    rec, turn = p1_check(rec, turn)
    usage_csv, usage_txt = measure_usage(rec, a.ai, a.session_log, PROJECT, stamp)
    put_evidence(rec, evidence(turn, read_at, "<THIS-COMMIT>", "ls-remote main = local head",
                               usage_txt, a.research, a.gaps))
    add_timeline(rec, *timeline_line(rec, turn, a.ai, a.summary or a.topic))
    tracked = set(out("ls-files").splitlines())
    stage = sorted({f for f in files if os.path.exists(f) or f in tracked}  # deletions of tracked files count
                   | {rec, TIMELINE} | ({usage_csv} if usage_csv else set()))
    idre = re.compile(rf"^{re.escape(CFG['prefix'])}\d+-")
    stage = [f for f in stage if f == rec or not (f.startswith(CFG["records_root"] + "/")
             and idre.match(os.path.basename(f)) and f not in tracked)]  # drop our pre-rename name
    scan = subprocess.run([sys.executable, "-I", CFG["secret_scan"], *[f for f in stage if os.path.exists(f)]], capture_output=True, text=True)
    print(scan.stdout.strip(), file=sys.stderr)
    if scan.returncode:
        raise Stop(2, "secret scan found a blocking hit — nothing committed")
    git("add", "-A", "--", *stage)
    msg = CFG["commit_format"].format(ai=a.ai, turn=turn, topic=a.topic) + ("\n\n" + "\n".join(a.trailer) if a.trailer else "")
    git("commit", "-q", "-m", msg)
    return rec, turn, usage_txt, out("rev-parse", "HEAD")


def main():
    global REPO, PROJECT
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--turn", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--ai", required=True)
    ap.add_argument("--session-log", default=None)
    ap.add_argument("--research", default="none")
    ap.add_argument("--gaps", default="none")
    ap.add_argument("--record", default=None)
    ap.add_argument("--summary", default=None, help="timeline text (default: --topic)")
    ap.add_argument("--trailer", action="append", default=[])
    a = ap.parse_args()
    if a.session_log is None:
        logs = sorted(glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl")), key=os.path.getmtime)
        a.session_log = logs[-1] if logs else None
    url = out("remote", "get-url", "origin")
    REPO = re.sub(r"(\.git)?/?$", "", re.sub(r"^.*github\.com[:/]", "", url)) if "github.com" in url else os.path.basename(url)
    PROJECT = os.path.basename(REPO)  # may be replaced by the "project" setting in load_cfg
    stamp = dt.datetime.now(TZ).strftime("%Y%m%d_%H%M")

    try:
        load_cfg()
        files = changed_files()  # what this turn changed, captured before any pull
        rec = find_record(a.turn, a.record)
        turn = a.turn
        sync(None)
        read_at = fill_read_at(rec, out("rev-parse", "--short", "HEAD"))
        commit, hook = None, os.environ.get(HOOK)
        for attempt in range(1, 4):
            rec, turn, usage_txt, commit = prepare(a, rec, turn, read_at, files, stamp)
            if hook:
                subprocess.run(hook, shell=True); hook = None
            if git("push", "origin", "HEAD:main", check=False).returncode == 0:
                break
            log(f"push rejected (try {attempt}/3) — pulling and redoing the commit")
            sync(commit)
            files = list(set(files) | set(changed_files()))
        else:
            raise Stop(3, "push failed 3 times — commit kept locally, not forced")
        remote = out("ls-remote", "origin", "refs/heads/main").split()[0]
        local = out("rev-parse", "HEAD")
        if remote != local:
            raise Stop(4, f"verify failed: ls-remote {remote[:7]} != local {local[:7]}")
        print(evidence(turn, read_at, local[:7], f"ls-remote main = local head ({local[:7]})",
                       usage_txt, a.research, a.gaps))
        return 0
    except Stop as e:
        log(f"STOP ({e.code}): {e}")
        return e.code


REPO = PROJECT = ""
if __name__ == "__main__":
    sys.exit(main())
