#!/usr/bin/env python3
# Copied from vsenthil7/claude-history-workbench @ 0c1ee3e on 2026-10-18 (chatgpt-history T002).
"""
Per-turn token usage for one Claude cloud session, from its transcript
(~/.claude/projects/<dir>/<session>.jsonl). MEASURED, not estimated:
these are the usage numbers the API returned for each model call.

A "turn" starts at each real Senthil message (not tool results / system notes).
Each model call is counted once (deduplicated by message id).

Effective units = input + 0.1*cache_read + 2*cache_write + 5*output
(relative cost weights in "regular input token" units; approximate).

Usage: python3 -I usage_session.py <session.jsonl> <out_csv>
Prints a markdown table; writes the CSV.
"""
import csv, json, sys

src, out = sys.argv[1], sys.argv[2]
turns, cur, seen = [], None, set()


def is_real_user(d):
    if d.get("type") != "user" or d.get("isMeta") or d.get("toolUseResult") is not None:
        return False
    c = d.get("message", {}).get("content")
    if isinstance(c, list):
        if any(x.get("type") == "tool_result" for x in c):
            return False
        txt = " ".join(x.get("text", "") for x in c if x.get("type") == "text")
    else:
        txt = c or ""
    # skip harness-injected messages (system reminders only, file-delivery notes, skill bodies)
    body = txt.split("</system-reminder>")[-1].strip()
    return bool(body) and not body.startswith(("The files from earlier", "Show me where this session's tokens", "Tool loaded"))


for line in open(src, encoding="utf-8"):
    d = json.loads(line)
    if is_real_user(d):
        cur = dict(turn_start_utc=d["timestamp"], calls=0, input=0, cache_read=0, cache_write=0, output=0)
        turns.append(cur)
    elif d.get("type") == "assistant" and cur is not None:
        m = d.get("message", {})
        mid, u = m.get("id"), m.get("usage") or {}
        if not mid or mid in seen or u.get("output_tokens") is None:
            continue
        seen.add(mid)
        cur["calls"] += 1
        cur["input"] += u.get("input_tokens") or 0
        cur["cache_read"] += u.get("cache_read_input_tokens") or 0
        cur["cache_write"] += u.get("cache_creation_input_tokens") or 0
        cur["output"] += u.get("output_tokens") or 0

for t in turns:
    t["effective_units"] = round(t["input"] + 0.1 * t["cache_read"] + 2 * t["cache_write"] + 5 * t["output"])

with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(turns[0].keys())); w.writeheader(); w.writerows(turns)

print("| turn start (UTC) | model calls | input | cache read | cache write | output | effective units |")
print("|---|---|---|---|---|---|---|")
tot = {k: 0 for k in ("calls", "input", "cache_read", "cache_write", "output", "effective_units")}
for t in turns:
    print(f"| {t['turn_start_utc'][:16]} | {t['calls']} | {t['input']:,} | {t['cache_read']:,} | {t['cache_write']:,} | {t['output']:,} | {t['effective_units']:,} |")
    for k in tot: tot[k] += t[k]
print(f"| **total** | {tot['calls']} | {tot['input']:,} | {tot['cache_read']:,} | {tot['cache_write']:,} | {tot['output']:,} | {tot['effective_units']:,} |")
