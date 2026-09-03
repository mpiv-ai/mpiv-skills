#!/usr/bin/env python3
"""Scaffold a new MPIV skill from the template.

Usage: python3 skills/mpiv-skill-creator/scripts/new_skill.py <skill-name> [--root <library-root>]

Creates skills/<skill-name>/ with SKILL.md, README.md, evals/evals.json and the
empty references/, assets/, examples/, scripts/ folders. Exit 1 if the name
breaks the Agent Skills spec or the folder already exists. Standard library only.
"""
import datetime
import os
import re
import shutil
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    name = argv[0]
    root = os.getcwd()
    if "--root" in argv:
        root = argv[argv.index("--root") + 1]
    if len(name) > 64 or not NAME_RE.match(name):
        print(f"bad name '{name}': lowercase letters, digits, single hyphens, 64 chars max")
        return 1
    here = os.path.dirname(os.path.abspath(__file__))
    template = os.path.join(here, "..", "assets", "skill-template")
    target = os.path.join(root, "skills", name)
    if os.path.exists(target):
        print(f"exists: {target}")
        return 1
    today = datetime.date.today().isoformat()
    os.makedirs(os.path.join(target, "evals"))
    for d in ("references", "assets", "examples", "scripts"):
        os.makedirs(os.path.join(target, d))
        open(os.path.join(target, d, ".gitkeep"), "w").close()
    for src, dst in (("SKILL.md", "SKILL.md"), ("README.md", "README.md"), ("evals.json", os.path.join("evals", "evals.json"))):
        with open(os.path.join(template, src)) as f:
            s = f.read()
        s = s.replace("{skill-name}", name).replace("{YYYY-MM-DD}", today)
        with open(os.path.join(target, dst), "w") as f:
            f.write(s)
    print(f"created {target}")
    print("next: fill SKILL.md, delete any folder the skill does not earn, then run check_skill.py")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
