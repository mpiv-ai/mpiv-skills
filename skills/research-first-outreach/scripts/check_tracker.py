#!/usr/bin/env python3
"""Check an outreach tracker CSV and report reply and booking rates per cohort.

Usage: python3 scripts/check_tracker.py path/to/tracker.csv

Standard library only. Exit code 1 when any row fails a check, so the script
can gate a send batch.
"""
import csv
import sys
from collections import defaultdict

REQUIRED = ["first_name", "email", "company", "site", "observation", "segment", "cohort", "variant", "status"]
STATUSES = ["identified", "drafted", "sent", "replied", "booked", "closed"]
OPENERS = ("I saw that", "I noticed", "Your")
PRAISE = ("impressive", "love", "great", "amazing", "incredible", "awesome", "fantastic")


def main(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("no rows")
        return 1
    missing_cols = [c for c in REQUIRED if c not in rows[0]]
    if missing_cols:
        print("missing columns:", ", ".join(missing_cols))
        return 1
    problems = 0
    per_cohort = defaultdict(lambda: {"sent": 0, "replied": 0, "booked": 0})
    for i, r in enumerate(rows, start=2):
        errs = []
        for c in REQUIRED:
            if not (r.get(c) or "").strip():
                errs.append(f"empty {c}")
        obs = (r.get("observation") or "").strip()
        if obs and not obs.startswith(OPENERS):
            errs.append("observation does not start with 'I saw that', 'I noticed', or 'Your'")
        low = obs.lower()
        hits = [w for w in PRAISE if w in low]
        if hits:
            errs.append("observation contains praise: " + ", ".join(hits))
        if r.get("status") and r["status"] not in STATUSES:
            errs.append(f"unknown status '{r['status']}'")
        if r.get("status") == "sent" and not (r.get("first_sent_at") or "").strip():
            errs.append("status sent but first_sent_at empty")
        if errs:
            problems += 1
            print(f"row {i} ({r.get('first_name','')} {r.get('last_name','')}): " + "; ".join(errs))
        st = r.get("status")
        c = per_cohort[r.get("cohort") or "?"]
        if st in ("sent", "replied", "booked", "closed"):
            c["sent"] += 1
        if st in ("replied", "booked"):
            c["replied"] += 1
        if st == "booked":
            c["booked"] += 1
    print()
    print("cohort  sent  replied  booked  reply_rate")
    for k in sorted(per_cohort):
        c = per_cohort[k]
        rate = (c["replied"] / c["sent"]) if c["sent"] else 0.0
        print(f"{k:>6}  {c['sent']:>4}  {c['replied']:>7}  {c['booked']:>6}  {rate:>9.0%}")
    print()
    print(f"{len(rows)} rows, {problems} with problems")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
