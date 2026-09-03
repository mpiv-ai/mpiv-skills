#!/usr/bin/env python3
"""Check an MPIV skill folder against the Agent Skills spec and the library conventions.

Usage: python3 skills/mpiv-skill-creator/scripts/check_skill.py skills/<skill-name> [more paths]

Checks: frontmatter is first, name matches the directory and the spec pattern,
description length, SKILL.md under 500 lines, provenance block and changelog
present, every relative link in SKILL.md resolves, evals/evals.json parses with
the required keys, no template placeholders left, no banned phrases, no em
dashes (code blocks and inline code are skipped). Exit 1 on any failure. Standard library only.
"""
import json
import os
import re
import sys

NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
BANNED = [
    "honestly", "to be honest", "load-bearing", "load bearing", "let's dive in", "game changer",
    "game-changer", "seamless", "robust", "it is worth noting", "it's worth noting", "worth noting",
    "at its core", "at the end of the day", "needless to say", "in conclusion", "ultimately",
    "furthermore", "moreover", "additionally", "here's the thing", "here is the thing",
    "the real question", "the whole trick", "the key takeaway", "make no mistake", "that said",
    "delve", "leverage", "landscape", "crucial", "pivotal", "journey", "empower", "unlock",
    "deep dive", "treasure trove", "elevate", "streamline", "harness the power", "not just",
    "it's not about", "it is not about", "actually",
]
PLACEHOLDER = re.compile(r"\{[a-z][a-z0-9 -]*\}")
LINK = re.compile(r"\]\(([^)#]+)\)")


def check(path):
    errs, warns = [], []
    path = path.rstrip("/")
    skill_md = os.path.join(path, "SKILL.md")
    if not os.path.isfile(skill_md):
        return [f"{path}: no SKILL.md"], []
    text = open(skill_md).read()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errs.append("frontmatter must start on line 1")
        fm = ""
    else:
        try:
            end = lines[1:].index("---") + 1
        except ValueError:
            errs.append("frontmatter has no closing ---")
            end = 0
        fm = "\n".join(lines[1:end])
    m = re.search(r"^name:\s*(.+)$", fm, re.M)
    name = m.group(1).strip() if m else ""
    dirname = os.path.basename(path)
    if not name:
        errs.append("frontmatter: name missing")
    else:
        if name != dirname:
            errs.append(f"frontmatter name '{name}' != directory '{dirname}'")
        if len(name) > 64 or not NAME_RE.match(name):
            errs.append("name breaks the spec pattern (lowercase, digits, single hyphens, 64 max)")
    m = re.search(r"^description:\s*(.+)$", fm, re.M)
    desc = m.group(1).strip() if m else ""
    if not desc:
        errs.append("frontmatter: description missing")
    elif len(desc) > 1024:
        errs.append(f"description is {len(desc)} chars; spec max 1024")
    for key in re.findall(r"^([A-Za-z-]+):", fm, re.M):
        if key not in ("name", "description", "license", "compatibility", "metadata", "allowed-tools",
                       "disable-model-invocation", "user-invocable", "disallowed-tools", "model",
                       "context", "agent", "background", "arguments", "paths", "hooks", "when_to_use"):
            warns.append(f"frontmatter key '{key}' is not in the spec or the Claude Code extensions")
    if len(lines) > 500:
        errs.append(f"SKILL.md is {len(lines)} lines; keep under 500")
    if "## Provenance" not in text:
        errs.append("missing '## Provenance' block")
    if "### Changelog" not in text:
        errs.append("missing '### Changelog'")
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not os.path.exists(os.path.join(path, target)):
            errs.append(f"link target missing: {target}")
    ph = sorted(set(PLACEHOLDER.findall(text)))
    if ph:
        errs.append("template placeholders left: " + ", ".join(ph[:6]))
    evals = os.path.join(path, "evals", "evals.json")
    if not os.path.isfile(evals):
        errs.append("missing evals/evals.json")
    else:
        try:
            ev = json.load(open(evals))
            if ev.get("skill_name") != name:
                errs.append("evals.json skill_name does not match frontmatter name")
            cases = ev.get("evals", [])
            if len(cases) < 2:
                warns.append(f"evals.json has {len(cases)} case(s); aim for 2 or 3")
            for c in cases:
                for k in ("id", "prompt", "expected_output", "expectations"):
                    if k not in c:
                        errs.append(f"evals.json case {c.get('id','?')} missing '{k}'")
        except json.JSONDecodeError as e:
            errs.append(f"evals.json does not parse: {e}")
    prose_files = [skill_md, os.path.join(path, "README.md")]
    for sub in ("references", "examples"):
        d = os.path.join(path, sub)
        if os.path.isdir(d):
            prose_files += [os.path.join(d, f) for f in os.listdir(d) if f.endswith(".md")]
    for f in prose_files:
        if not os.path.isfile(f):
            continue
        body = open(f).read()
        body = re.sub(r"```.*?```", "", body, flags=re.S)
        body = re.sub(r"`[^`\n]*`", "", body)
        if "—" in body:
            errs.append(f"{os.path.relpath(f, path)}: em dash present")
        low = body.lower()
        hits = [b for b in BANNED if re.search(r"\b" + re.escape(b) + r"\b", low)]
        if hits:
            errs.append(f"{os.path.relpath(f, path)}: banned phrases: " + ", ".join(hits))
    for sub in ("references", "assets", "examples", "scripts"):
        d = os.path.join(path, sub)
        if os.path.isdir(d) and not [x for x in os.listdir(d) if x != ".gitkeep"]:
            warns.append(f"{sub}/ is empty; delete it or fill it")
    return errs, warns


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    failed = 0
    for p in argv:
        errs, warns = check(p)
        print(f"== {p}")
        for w in warns:
            print("  warn:", w)
        for e in errs:
            print("  FAIL:", e)
        if not errs:
            print("  ok")
        failed += bool(errs)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
