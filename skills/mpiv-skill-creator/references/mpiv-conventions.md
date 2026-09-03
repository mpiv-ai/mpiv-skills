# MPIV conventions

What this library adds on top of the spec and the Claude Code docs.

## The provenance block

Every SKILL.md ends with this table and a changelog. It is how a reader knows the method has run and what it produced.

```
## Provenance

| Field | Value |
|---|---|
| Origin | Where the method came from: campaign, engagement, person, date |
| First run | Date and scale: "2026-08-31, 20 emails in two cohorts" |
| Result | The numbers: replies, calls, files, pass rate |
| Evidence | Where the proof lives: the examples file, a CRM, a mailbox, a repo path |
| Added to library | Date |

### Changelog

- YYYY-MM-DD: what changed, and the eval pass rate with and without the skill when it was measured.
```

A skill that has not run yet says "First run: none yet" and stays out of the README table.

## Voice

Skills are MPIV prose. The rules in `~/.claude/voice.md` apply to SKILL.md, references, README, and examples, the same as to an email. In short:

- Lead with what the skill produces. Evidence next to the claim. Plain verbs.
- No em dashes. No contrast constructions of the "it is less X than Y" kind. No sentence whose job is to land, contrast, or announce candor.
- No filler intensifiers, no performed-candor openers, no flourish vocabulary. The phrase list lives in `BANNED` inside `scripts/check_skill.py`; the checker fails a skill that uses one outside a code block.
- Explain why a rule exists. Capitals and all-caps imperatives are a sign the reason is missing.
- Numbers go in a table.

The checker catches the list. The rest is a reread of every paragraph.

## What stays out of a public skill

- Real prospect, client, or participant names, firms, and email addresses. Roles, dates, and outcomes are fine.
- Michael's postal address and booking URL; use `{placeholders}` in assets.
- Credentials, API keys, CRM record ids.
- Dependencies. A script that needs `pip install` will not be run; standard library only.
- Client material of any kind. Examples are redacted reconstructions of MPIV's own runs.

## Layout

```
skills/<name>/
├── SKILL.md
├── README.md
├── references/
├── assets/
├── examples/
├── scripts/
└── evals/evals.json
```

Only folders the skill earns. `references/` for detail a step needs in full; `assets/` for files the user fills; `examples/` for one redacted run; `scripts/` for mechanical checks; `evals/` always.

## Registration

1. README table row: `| [name](skills/name/SKILL.md) | one sentence | run it came from |`.
2. Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
3. Changelog line in the skill.
4. Commit and push are Michael's: `git -c user.name="Michael Isaac" -c user.email="michael@mpiv.ai" commit`.
