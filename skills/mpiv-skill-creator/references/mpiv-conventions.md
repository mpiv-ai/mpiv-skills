# MPIV conventions

What this library adds on top of the spec and the Claude Code docs.

## The provenance block

Every SKILL.md ends with this table and a changelog. A reader uses it to see that the method has run and what it produced.

```
## Provenance

| Field | Value |
|---|---|
| Origin | Where the method came from: campaign, engagement, person, date |
| First run | Date and scale: "31 Aug 2026, 20 emails in two cohorts" |
| Result | The numbers: replies, calls, files, pass rate |
| Evidence | Where the proof is: the examples file, a CRM, a mailbox, a repo path |
| Added to library | Date |

### Changelog

- YYYY-MM-DD: what changed. Include the eval pass rate with and without the skill when measured.
```

A skill that has not run says "First run: none yet" and stays out of the README table.

## Writing rules

Skill files are MPIV prose. The rules in `~/.claude/voice.md` apply to SKILL.md, references, README, and examples, the same as to an email. Michael rejected two versions of library files on 3 September 2026 for reading like AI writing. The second rejection came after the ban-list check passed, so the list is not enough. Reread every paragraph against these:

- Short sentences. One fact or one instruction per sentence.
- Say what to do and what happened. Do not explain why with a general truth. "Write the limit column on day one. On the first run an export never arrived, and the inventory carried that gap from the week it was due" is fine. "The limit column is the one people skip and the one the client reads" is not.
- No contrast pairs: "X, not Y", "not X but Y", "X is Y; Z is not".
- No lines built to be quoted. If a sentence would work as a caption, cut it or turn it into a plain instruction.
- No sentence whose only job is to close a section.
- No em dashes.
- No filler intensifiers, no performed-candor openers, no flourish vocabulary. The phrase list is `BANNED` in `scripts/check_skill.py`. The checker fails a skill that uses one outside a code block.
- Numbers go in a table.

## What stays out of a public skill

- Real prospect, client, or participant names, firms, and email addresses. Roles, dates, and outcomes can stay.
- Michael's postal address and booking URL. Use placeholders in assets.
- Credentials, API keys, CRM record ids.
- Dependencies. A script that needs `pip install` will not be run. Standard library only.
- Client material. Examples are redacted reconstructions of MPIV's own runs.

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

Include only the folders the skill uses. `references/` for detail a step needs in full. `assets/` for files the user fills. `examples/` for one redacted run. `scripts/` for mechanical checks. `evals/` always.

## Registration

1. README table row: `| [name](skills/name/SKILL.md) | one sentence | run it came from |`.
2. Bump `version` in both `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
3. Changelog line in the skill.
4. Michael commits and pushes: `git -c user.name="Michael Isaac" -c user.email="michael@mpiv.ai" commit`.
