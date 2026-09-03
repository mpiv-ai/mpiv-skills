#!/usr/bin/env python3
"""Check a findings table against its source inventory and the hour ledger.

Usage: python3 scripts/check_evidence.py source-inventory.csv findings-table.md hour-ledger.csv

Fails (exit 1) when a finding row has no source id in its evidence cell, cites
an id not in the inventory, when an inventory source is never cited, or when a
week's hours exceed its cap (authorized_cap when set, else cap). Standard
library only.
"""
import csv
import re
import sys

ID_RE = re.compile(r"\[(S\d+)\]")


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main(inv_path, table_path, ledger_path):
    problems = 0
    inventory = {r["id"].strip() for r in read_rows(inv_path) if r.get("id")}
    if not inventory:
        print("inventory has no ids")
        return 1
    cited = set()
    findings = 0
    for line in open(table_path):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4 or not re.match(r"^F\d+$", cells[0]):
            continue
        findings += 1
        ids = set(ID_RE.findall(cells[2]))
        if not ids:
            problems += 1
            print(f"{cells[0]}: no source id in the evidence cell")
        unknown = ids - inventory
        if unknown:
            problems += 1
            print(f"{cells[0]}: cites ids not in the inventory: {', '.join(sorted(unknown))}")
        cited |= ids
    if findings == 0:
        problems += 1
        print("no finding rows (F1, F2, ...) found in the table")
    uncited = inventory - cited
    for s in sorted(uncited):
        problems += 1
        print(f"{s}: in the inventory but never cited")
    over = 0
    weeks = read_rows(ledger_path)
    for w in weeks:
        try:
            hours = float(w.get("hours") or 0)
            cap = float(w.get("authorized_cap") or w.get("cap") or 0)
        except ValueError:
            problems += 1
            print(f"week {w.get('week_start')}: hours or cap not a number")
            continue
        if cap and hours > cap:
            over += 1
            problems += 1
            print(f"week {w.get('week_start')}: {hours:g} hours over cap {cap:g}")
    total = sum(float(w.get("hours") or 0) for w in weeks)
    print()
    print(f"{findings} findings, {len(inventory)} sources, {len(cited)} cited, {len(uncited)} uncited")
    print(f"{len(weeks)} weeks logged, {total:g} hours, {over} over cap")
    print(f"{problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(*sys.argv[1:]))
