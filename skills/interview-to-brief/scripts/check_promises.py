#!/usr/bin/env python3
"""List open promises from the Delivery table in a findings file.

Usage: python3 scripts/check_promises.py path/to/findings.md

Reads the first markdown table under a '## Delivery' heading whose header has
Promise, Artifact, and Status columns. Prints every row whose status is not
Done, Live, or Sent. Exit 1 when open rows remain, 0 when none, 2 when the
table is missing. Standard library only.
"""
import re
import sys

CLOSED = ("done", "live", "sent")


def main(path):
    text = open(path).read()
    m = re.search(r"^## Delivery.*?$", text, re.M)
    if not m:
        print("no '## Delivery' heading")
        return 2
    rows = []
    for line in text[m.end():].splitlines():
        if line.startswith("## "):
            break
        if line.startswith("|"):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    if len(rows) < 3:
        print("no table under '## Delivery'")
        return 2
    header = [h.lower() for h in rows[0]]
    try:
        ip, ia, istat = header.index("promise"), header.index("artifact"), header.index("status")
    except ValueError:
        print("table needs Promise, Artifact, Status columns")
        return 2
    open_rows = []
    for r in rows[2:]:
        if len(r) <= istat:
            continue
        status = r[istat].lower()
        if not any(status.startswith(c) for c in CLOSED):
            open_rows.append(r)
    for r in open_rows:
        print(f"OPEN  {r[ip]}  ->  {r[istat]}")
    print(f"{len(rows) - 2} promises, {len(open_rows)} open")
    return 1 if open_rows else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
