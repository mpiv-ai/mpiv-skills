---
name: mpiv-skill-creator
description: Turn a consulting method that has already run on real work into a new skill in the MPIV skill library, laid out and checked against the current Agent Skills spec and Claude Code plugin rules. Use this whenever the user says "make this a skill", "add this to the library", "new skill", "skill from this workflow", "package this method", or asks how MPIV skills should be structured. Also use it to check or update an existing MPIV skill. It scaffolds the folder, writes SKILL.md in plain English, adds references, assets, examples, evals, and scripts where they are needed, runs the checks, and registers the skill in the library README.
---

# MPIV skill creator

A skill in this library is a method that has run on real work, written down so an agent can run it again, with the results of the first run attached. This skill turns one method into a folder under `skills/` that loads in Claude Code and in other agents that read the Agent Skills format.

Read both reference files before writing anything:

- [references/official-guidance.md](references/official-guidance.md): spec limits, Claude Code frontmatter fields, plugin layout rules, the eval format, and the validation commands. Each rule has its source URL and the date it was checked. If that date is more than a month old, re-fetch the sources first.
- [references/mpiv-conventions.md](references/mpiv-conventions.md): the provenance block, the writing rules, what stays out of a public skill, and how a skill gets registered.

## Step 0: qualify

Ask, or read from the conversation:

1. Has this method run on real work at least once? When, and what happened? If not, you can still write the skill, but the provenance block says "First run: none yet" and the README table does not list it until it has run.
2. What phrases would a user say when they need it? These go in the description.
3. What are the inputs, the steps, the outputs, and the two most common failure points?
4. What did the run leave behind that a future run would have to rebuild: a template, a checklist, a query list, a script? Those become assets and scripts.
5. What must stay out: client names, personal data, addresses, credentials, anything a participant did not agree to.

If the user cannot answer 1 and 2, stop. Help them get a run done first.

## Step 1: scaffold

From the library root:

```
python3 skills/mpiv-skill-creator/scripts/new_skill.py <skill-name>
```

Name rules from the spec: lowercase letters, digits, and hyphens; no leading, trailing, or double hyphens; 64 characters or fewer; the frontmatter name equals the directory name. Name the skill for what it does.

The scaffolder creates:

```
skills/<skill-name>/
├── SKILL.md            # steps, files list, provenance, changelog
├── README.md           # one paragraph, install line, link to SKILL.md
├── references/         # detail a step needs in full
├── assets/             # templates the user fills: CSV, HTML, docx
├── examples/           # one redacted real run with the numbers
├── scripts/            # mechanical checks only, standard library only
└── evals/evals.json    # 2 to 3 prompts with expectations
```

Delete any folder the skill does not use. Do not leave empty folders.

## Step 2: write SKILL.md

Order: one paragraph on what the skill produces and where it came from; numbered steps; a files list that says when to read each file; the provenance block; the changelog.

Writing rules, with the reason for each:

- The description does the triggering. State what the skill does, then the phrases users say, then the contexts. Claude under-triggers skills, so list more phrases than feels necessary. Keep it under 1024 characters. Claude Code caps each listing entry at 1,536 characters and trims the least-used skills first when the listing is over budget.
- Keep SKILL.md under 500 lines. Move detail into `references/` and say in the files list when to open each one. The body loads in full when the skill fires and stays in context for the rest of the task. References load only when read.
- Write instructions that hold for the whole task as standing rules, not as one-time steps. Claude Code does not re-read the file on later turns.
- Give the reason for each rule. Do not write rules in capitals. A model that knows the reason can handle the case the rule did not cover.
- Use the spec's six frontmatter fields unless a Claude Code field is needed. Use `disable-model-invocation: true` for skills with side effects the user should time (send, deploy, publish). Use `allowed-tools` only to pre-approve a bundled script, with the `${CLAUDE_SKILL_DIR}` pattern.
- Put the numbers from the run in the file: how many, how long, what came back.
- Write in plain English. Short sentences. Facts and instructions. No maxims, no contrast pairs, no lines written to sound wise. The full rules are in [references/mpiv-conventions.md](references/mpiv-conventions.md).

## Step 3: fill the folders

- **references/**: one file per topic a step needs in full: the exact template, the query list, the checklist. Under 300 lines each, or add a table of contents.
- **assets/**: files the user copies and fills. Placeholders in curly braces. No real names, addresses, or URLs that belong to Michael or a participant.
- **examples/**: the first run, redacted. A timeline with dates, the artifact that worked, the numbers as a table. Remove people and firms. Keep roles, dates, and outcomes.
- **scripts/**: mechanical work only: validate a file, compute a rate, render a template. Standard library only, one file, a docstring with the usage line, exit code 1 on failure. If a script would do the judgment part of the skill, the skill is not written down yet.
- **evals/evals.json**: two or three prompts a real user would type, one of them an edge case. Each has `expected_output` and a list of `expectations` a grader can check. Format in the guidance file.

## Step 4: check

From the library root:

```
python3 skills/mpiv-skill-creator/scripts/check_skill.py skills/<skill-name>
claude plugin validate .
npx -y skills add . --list
```

The first script checks the frontmatter against the spec, the line count, the provenance block, that every file named in SKILL.md exists, that `evals.json` parses, and that no banned phrases appear. The second is Claude Code's validator. The third confirms the skills CLI can see the skill. On 3 September 2026 the CLI skipped a skill whose description had a colon followed by a space; the validator had passed it. Fix everything before moving on. A warning from `claude plugin validate` about an unknown field means the field is ignored; remove it.

## Step 5: run the evals

Run each prompt in `evals/evals.json` twice in fresh subagents: once with the skill path, once without. Grade the expectations against the outputs, with evidence for each pass. The official `skill-creator` plugin (`/plugin install skill-creator@claude-plugins-official`) runs this loop and writes the report. Use it when installed. Record the pass rate with and without the skill in the changelog. If the expectations pass at the same rate without the skill, cut the skill down or remove it.

## Step 6: register

1. Add a row to the library `README.md` table: the skill name linked to its SKILL.md, one sentence on what it does, and the run it came from.
2. Bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together. Marketplace users get updates only when the version changes.
3. Add a changelog line in the skill's SKILL.md with the date.
4. Stop. Michael commits and pushes. Give him the commit command with the author set to `Michael Isaac <michael@mpiv.ai>`.

## Files

- [references/official-guidance.md](references/official-guidance.md): spec and docs rules with sources and the check date.
- [references/mpiv-conventions.md](references/mpiv-conventions.md): provenance block, writing rules, exclusions, registration.
- [assets/skill-template/](assets/skill-template/): the SKILL.md, README.md, and evals.json the scaffolder copies.
- [scripts/new_skill.py](scripts/new_skill.py): scaffold a skill folder from the template.
- [scripts/check_skill.py](scripts/check_skill.py): the checks in step 4.
- [evals/evals.json](evals/evals.json): test prompts for this skill.

## Provenance

| Field | Value |
|---|---|
| Origin | Built 3 Sep 2026 while adding research-first-outreach to the library |
| First run | 3 Sep 2026: added assets, examples, evals, a script, and a provenance block to research-first-outreach; then built interview-to-brief and evidence-synthesis |
| Result | All four skills pass `check_skill.py`, `claude plugin validate`, and the skills CLI listing |
| Evidence | c3-consulting-os/research/skill-library-distribution.md; the sources in references/official-guidance.md |
| Added to library | 2026-09-03 |

### Changelog

- 2026-09-03: first version. Later the same day: the checker flags colon-space in unquoted frontmatter values; prose rewritten in plain English.
