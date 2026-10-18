#!/usr/bin/env python3
# Copied from vsenthil7/claude-history-workbench @ 0c1ee3e on 2026-10-18 (chatgpt-history T002).
"""
Pre-commit secret scan (Git Turn Protocol v1.0, step 6).
Patterns taken from TalkProof AI Sessions Protocol v0 §11, plus Anthropic/Google/GitHub key shapes.

Usage:
  python3 -I secret_scan.py              scan files staged in the current repo
  python3 -I secret_scan.py <path>...    scan the given files/folders
Exit 0 = clean, 1 = hits (printed as file:line:pattern; the value itself is not printed).
Phone-like hits are warnings only (exit 0) — review by eye.
"""
import os
import re
import subprocess
import sys

BLOCK = {
    "openai/anthropic key": r"\bsk-(ant-)?[A-Za-z0-9_-]{20,}",
    "stripe webhook secret": r"whsec_[A-Za-z0-9]{8,}",
    "stripe live key": r"\b[sr]k_live_[A-Za-z0-9]{16,}",
    "aws access key": r"\bAKIA[0-9A-Z]{16}\b",
    "google api key": r"\bAIza[0-9A-Za-z_-]{35}\b",
    "github token": r"\bgh[pousr]_[A-Za-z0-9]{36,}\b",
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "bearer token": r"Bearer\s+[A-Za-z0-9._-]{20,}",
    "jwt": r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{5,}",
    "credentialed url": r"(postgres|postgresql|redis|mysql|mongodb)(\+\w+)?://[^\s:/]+:[^\s@]+@",
    "assigned secret": r"(?i)\b(password|passwd|secret|api_key|apikey|access_token)\s*[:=]\s*['\"]?[A-Za-z0-9/+_.-]{12,}",
}
WARN = {"phone-like": r"\+\d[\d \-]{9,}\d"}
ALLOW = ("[REDACTED", "EXAMPLE", "<", "xxxx", "your-", "YOUR_")


def files(args):
    if not args:
        out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                             capture_output=True, text=True, check=True).stdout.split()
        return [f for f in out if os.path.isfile(f)]
    res = []
    for a in args:
        if os.path.isdir(a):
            for root, _, fs in os.walk(a):
                if "/.git" in root:
                    continue
                res += [os.path.join(root, f) for f in fs]
        else:
            res.append(a)
    return res


hits = warns = 0
for f in files(sys.argv[1:]):
    try:
        lines = open(f, encoding="utf-8", errors="ignore").read().splitlines()
    except OSError:
        continue
    for n, line in enumerate(lines, 1):
        for name, pat in BLOCK.items():
            m = re.search(pat, line)
            if m and not any(a in m.group(0) for a in ALLOW):
                print(f"BLOCK {f}:{n}: {name}")
                hits += 1
        for name, pat in WARN.items():
            if re.search(pat, line):
                print(f"warn  {f}:{n}: {name} (check by eye)")
                warns += 1

print(f"secret_scan: {hits} blocking, {warns} warnings")
sys.exit(1 if hits else 0)
