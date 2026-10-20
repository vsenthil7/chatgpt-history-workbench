#!/usr/bin/env python3
"""
Extract the FINAL visible reply of every turn from a Claude cloud session log. [claude, T010]
Final reply = the assistant text blocks after the last tool call of the turn (what Senthil saw at the end),
plus every SendUserMessage sent during the turn (also seen by him, verbatim).
Turns start at each user message, INCLUDING harness messages such as stop-hook feedback (isMeta), so an
interruption shows up as its own turn. Tool results and plain system reminders do not start a turn.

Usage: python3 -I final_replies.py <session.jsonl> <out_dir>
Writes <out_dir>/<NN>_<HHMM>_input.txt, <NN>_<HHMM>_final_reply.txt and index.csv (UTC times).
Read-only on the log. Compare with each turn record's ASSISTANT RESPONSE block.
"""
import csv, json, os, sys

src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
turns, cur = [], None


def text_of(c):
    if isinstance(c, str):
        return c
    return "\n".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")


for line in open(src, encoding="utf-8"):
    d = json.loads(line)
    if d.get("type") == "user":
        c = d.get("message", {}).get("content")
        if isinstance(c, list) and any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
            continue
        body = text_of(c).split("</system-reminder>")[-1].strip()
        if not body or body.startswith(("Tool loaded", "The files from earlier")):
            continue
        cur = {"ts": d["timestamp"], "input": body, "meta": bool(d.get("isMeta")), "blocks": [], "sent": []}
        turns.append(cur)
    elif d.get("type") == "assistant" and cur is not None:
        for x in d.get("message", {}).get("content") or []:
            if x.get("type") == "text" and x.get("text", "").strip():
                cur["blocks"].append(("text", x["text"]))
            elif x.get("type") == "tool_use":
                cur["blocks"].append(("tool", x.get("name")))
                if x.get("name") == "SendUserMessage":
                    cur["sent"].append(x.get("input", {}).get("message", ""))

rows = []
for n, t in enumerate(turns, 1):
    last_tool = max([i for i, b in enumerate(t["blocks"]) if b[0] == "tool"], default=-1)
    final = "\n\n".join(b[1] for b in t["blocks"][last_tool + 1:] if b[0] == "text").strip()
    hhmm = t["ts"][11:13] + t["ts"][14:16]
    stem = f"{n:02d}_{hhmm}"
    open(os.path.join(out, f"{stem}_input.txt"), "w", encoding="utf-8").write(t["input"])
    full = final + ("\n\n--- SendUserMessage during the turn ---\n\n" + "\n\n---\n\n".join(t["sent"]) if t["sent"] else "")
    open(os.path.join(out, f"{stem}_final_reply.txt"), "w", encoding="utf-8").write(full)
    rows.append([n, t["ts"], "harness" if t["meta"] else "senthil", len(t["input"]), len(final), len(t["sent"]),
                 t["input"][:60].replace("\n", " ")])
with open(os.path.join(out, "index.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, lineterminator="\n")
    w.writerow(["n", "start_utc", "from", "input_chars", "final_reply_chars", "sendusermessage_count", "input_start"])
    w.writerows(rows)
for r in rows:
    print(r)
