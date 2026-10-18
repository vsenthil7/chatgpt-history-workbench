#!/usr/bin/env python3
"""
S7 + S8: readable chats and chat indexes, built ONLY from files already in Git. [claude, T006]
Mirrors claude-history-workbench readable/ (same header + "### 0001 · SPEAKER · time" layout).

Reads raw/conversations/**.json (already redacted) and index/files_<exportdate>.csv, writes:
  readable/conversations/YYYY/MM/<same stem>.md   DERIVED: text VERBATIM; thoughts VERBATIM (labelled);
                                                  voice transcripts VERBATIM; images/audio/attachments as links
  index/conversations.csv                         one row per chat (counts, project id, paths, size ESTIMATE)
  index/missing_files_<date>.csv                  files a chat references that the export does not contain
  index/projects.csv                              ChatGPT Project ids (conversation_template_id g-p-…) with chat counts
Message order = the chat's main branch: walk current_node → parent → … → root, then reverse.

Usage: python3 -I make_readable.py <repo_dir> <exportdate YYYYMMDD>
Rerunnable: rewrites readable/ and the two index files from raw/ every time (raw/ is never touched).
"""
import csv, datetime as dt, glob, json, os, sys
from collections import defaultdict

REPO, TAG = sys.argv[1], sys.argv[2]
files = {}
for r in csv.DictReader(open(os.path.join(REPO, "index", f"files_{TAG}.csv"), encoding="utf-8")):
    fid = r["entry"][:-4] if r["entry"].endswith(".dat") else r["entry"]
    files[fid] = r


def iso(t):
    return dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if t else "-"


MISSING = {}  # file id -> [name, first chat id, first chat raw path, references]
CUR = {}


def file_ref(fid, up, label=None):
    r = files.get(fid)
    if not r:
        e = MISSING.setdefault(fid, [label or "", CUR.get("id"), CUR.get("raw"), 0])
        e[0] = e[0] or (label or ""); e[3] += 1
        return f"`{label or fid}` (not in this export)"
    name = label or r["real_name"] or os.path.basename(r["stored_path"] or fid)
    if r["location"] == "git":
        return f"[{name}](<{up}{r['stored_path']}>)"
    return f"`{name}` (Drive-only — see index/large_files.csv or index/held_back_files.csv)"


def pointer_id(ptr):
    return (ptr or "").split("://", 1)[-1]


def render_part(p, up, out):
    if isinstance(p, str):
        if p.strip():
            out.append(p)
        return
    ct = p.get("content_type")
    if ct == "image_asset_pointer":
        out.append(f"[image: {file_ref(pointer_id(p.get('asset_pointer')), up)} · {p.get('width')}×{p.get('height')}]")
    elif ct == "audio_transcription":
        out.append(f"> voice transcript ({p.get('direction') or '-'}): {p.get('text') or ''}")
    elif ct == "audio_asset_pointer":
        out.append(f"[audio: {file_ref(pointer_id(p.get('asset_pointer')), up)}]")
    elif ct == "real_time_user_audio_video_asset_pointer":
        a = (p.get("audio_asset_pointer") or {}).get("asset_pointer")
        out.append(f"[voice/video turn, audio: {file_ref(pointer_id(a), up)}]")
    else:
        out.append(f"[{ct} part — see raw]")


rows, projects = [], defaultdict(list)
for raw in sorted(glob.glob(os.path.join(REPO, "raw", "conversations", "*", "*", "*.json"))):
    c = json.load(open(raw, encoding="utf-8"))
    rel_raw = os.path.relpath(raw, REPO).replace("\\", "/")
    y, m, stem = rel_raw.split("/")[2], rel_raw.split("/")[3], os.path.basename(raw)[:-5]
    rel_md = f"readable/conversations/{y}/{m}/{stem}.md"
    up = "../../../../"
    CUR.update(id=c.get("conversation_id"), raw=rel_raw)
    mp, chain, node = c["mapping"], [], c.get("current_node")
    seen = set()
    while node and node in mp and node not in seen:
        seen.add(node); chain.append(mp[node]); node = mp[node].get("parent")
    chain.reverse()
    proj = c.get("conversation_template_id") or ""
    L = [f"# {c.get('title') or '(untitled)'}", "",
         f"- conversation_id: `{c.get('conversation_id')}`",
         f"- created: {iso(c.get('create_time'))}  ·  updated: {iso(c.get('update_time'))}  ·  model: {c.get('default_model_slug') or '-'}",
         f"- ChatGPT Project id: `{proj}`" if proj else "- ChatGPT Project: none",
         f"- flags: archived={c.get('is_archived')} · starred={c.get('is_starred')} · do-not-remember={c.get('is_do_not_remember')}",
         f"- raw: [{os.path.basename(raw)}](<{up}{rel_raw}>)",
         "- provenance: DERIVED from raw file (text, thoughts and voice transcripts VERBATIM; images/audio/attachments as links; "
         "raw carries any logged redactions — see source/REDACTIONS.md)", "", "## Messages", ""]
    n = users = assistants = atts = chars = 0
    for nd in chain:
        msg = nd.get("message")
        if not msg:
            continue
        role = msg["author"]["role"]
        cont, md = msg["content"], msg.get("metadata") or {}
        body = []
        ty = cont.get("content_type")
        if ty in ("text", "multimodal_text"):
            for p in cont.get("parts") or []:
                render_part(p, up, body)
        elif ty == "thoughts":
            for t in cont.get("thoughts") or []:
                txt = (t.get("summary") or "") + ("\n" if t.get("summary") else "") + (t.get("content") or "")
                if txt.strip():
                    body.append("> thinking (as exported): " + txt.replace("\n", "\n> "))
        elif ty == "reasoning_recap":
            body.append(f"> reasoning recap: {cont.get('content') or ''}")
        else:
            body.append(f"[{ty} — see raw]")
        for a in md.get("attachments") or []:
            atts += 1
            body.append(f"- attachment: {file_ref(a.get('id'), up, a.get('name'))} · {a.get('mime_type') or '-'}")
        if not body:
            continue
        n += 1
        users += role == "user"; assistants += role == "assistant"
        text = "\n\n".join(body); chars += len(text)
        who = "SENTHIL" if role == "user" else ("CHATGPT" if role == "assistant" else role.upper())
        L += [f"### {n:04d} · {who} · {iso(msg.get('create_time'))}", "", text, ""]
    os.makedirs(os.path.join(REPO, os.path.dirname(rel_md)), exist_ok=True)
    with open(os.path.join(REPO, rel_md), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L).rstrip() + "\n")
    rows.append([c.get("conversation_id"), c.get("title") or "", iso(c.get("create_time")), iso(c.get("update_time")),
                 c.get("default_model_slug") or "", proj, c.get("is_archived"), c.get("is_starred"), n, users, assistants,
                 atts, chars, round(chars / 4), rel_raw, rel_md])
    if proj:
        projects[proj].append((iso(c.get("create_time")), c.get("title") or ""))

with open(os.path.join(REPO, "index", "conversations.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["conversation_id", "title", "created_utc", "updated_utc", "model", "project_id", "archived", "starred",
                "messages", "user_msgs", "assistant_msgs", "attachments", "readable_chars", "est_tokens_ESTIMATE",
                "raw_path", "readable_path"])
    w.writerows(sorted(rows, key=lambda r: r[2]))
with open(os.path.join(REPO, "index", "projects.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["project_id", "chats", "first_chat_utc", "last_chat_utc", "first_chat_title", "last_chat_title"])
    for p, v in sorted(projects.items(), key=lambda kv: -len(kv[1])):
        v.sort()
        w.writerow([p, len(v), v[0][0], v[-1][0], v[0][1], v[-1][1]])
with open(os.path.join(REPO, "index", f"missing_files_{TAG}.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["file_id", "name_if_known", "first_conversation_id", "first_raw_path", "references", "status"])
    for fid, (nm, cid, rp, k) in sorted(MISSING.items()):
        w.writerow([fid, nm, cid, rp, k, "UNRECOVERABLE from this export (referenced in chat, file not in zip)"])
print(f"missing files {len(MISSING)} (index/missing_files_{TAG}.csv)")
print(f"readable chats {len(rows)} · messages {sum(r[8] for r in rows):,} · attachments linked {sum(r[11] for r in rows):,}"
      f" · projects {len(projects)} · chars {sum(r[12] for r in rows):,}")
