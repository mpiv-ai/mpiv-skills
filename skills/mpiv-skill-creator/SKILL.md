---
name: mpiv-skill-creator
description: Turn a consulting workflow that has already run on real work into a new skill in the MPIV skill library, laid out and validated against the current Agent Skills spec and Claude Code plugin rules. Use this whenever the user says "make this a skill", "add this to the library", "new skill", "skill from this workflow", "package this method", or asks how MPIV skills should be structured. Also use it to check or upgrade an existing MPIV skill. It scaffolds the folder, writes SKILL.md in Michael's voice, adds references, assets, examples, evals, and scripts where they earn their place, runs the checks, and registers the skill in the library README.
---

# MPIV skill creator

A skill in this library is a method that has run on real work, written down so an agent can run it again, with the evidence from the first run attached. This skill turns one of those methods into a folder under `skills/` that loads in Claude Code and in every other agent that reads the Agent Skills spec.

Two files carry the rules. Read both before writing anything:

- [references/official-guidance.md](references/official-guidance.md): the spec limits, the Claude Code frontmatter extensions, the plugin layout rules, the eval format, and the validation commands, each with its source URL and the date it was checked. If that date is more than a month old, re-fetch the sources before relying on it.
- [references/mpiv-conventions.md](references/mpiv-conventions.md): what MPIV adds on top: the provenance block, the voice rules, what stays out of a public skill, and how a skill gets registered.

## Step 0: qualify

Ask, or read from the conversation, before scaffolding:

1. Has this method run on real work at least once? When, and what happened? A skill with no run and no numbers is a draft; it can be written, but the provenance block says so and the README table does not list it until it has run.
2. What triggers it? The phrases a user would say. These become the description.
3. What are the inputs, the steps, the outputs, and the two most common failure points?
4. What did the run leave behind that a future run would rebuild: a template, a checklist, a query list, a script? Those are the assets and scripts.
5. What must stay out: client names, personal data, addresses, credentials, anything the participant did not consent to.

If the user cannot answer 1 and 2, stop and help them get a run done first.

## Step 1: scaffold

Run the scaffolder from the library root. It copies the template and fills the name and date:

```
python3 skills/mpiv-skill-creator/scripts/new_skill.py <skill-name>
```

Name rules from the spec: lowercase letters, digits, hyphens; no leading, trailing, or double hyphens; 64 characters or fewer; the name in the frontmatter equals the directory name. Pick a name that says what the skill does, not who it is for.

The template produces:

```
skills/<skill-name>/
├── SKILL.md            # method, files list, provenance, changelog
├── README.md           # one paragraph, install line, link to SKILL.md
├── references/         # detail loaded when a step calls for it
├── assets/             # templates the user fills: CSV, HTML, docx
├── examples/           # one redacted real run with the numbers
├── scripts/            # mechanical checks only, standard library only
└── evals/evals.json    # 2 to 3 prompts with expectations
```

Delete any folder the skill does not earn. An empty `scripts/` is worse than none.

## Step 2: write SKILL.md

Structure that works, in this order: one paragraph on what the skill produces and why the method works; a numbered step sequence; a files list that says when to read each file; the provenance block; the changelog.

Writing rules that the spec and the docs give reasons for:

- The description does the triggering. Put what the skill does first, then the phrases users say, then the contexts. Claude tends to under-trigger, so lean toward listing more phrases than feels needed. Keep it under 1024 characters; Claude Code caps the listing entry at 1,536 characters and trims from the least-used skills when the listing overflows.
- Keep SKILL.md under 500 lines. Move detail into `references/` and say in the files list when to open each one. The body loads whole when the skill fires and stays in context for the rest of the task; references load only when read.
- Write standing instructions, not one-time steps, for anything that should hold through the task. Claude Code does not re-read the file on later turns.
- Explain why a rule exists instead of writing it in capitals. A model that knows the reason handles the case the rule did not foresee.
- Use the spec's six frontmatter fields unless a Claude Code extension is needed. `disable-model-invocation: true` for skills with side effects the user should time (send, deploy, publish). `allowed-tools` only to pre-approve a bundled script, with the `${CLAUDE_SKILL_DIR}` pattern so it runs without a prompt.
- Put the numbers from the run in the file. A skill that says "one reply in ten" is used; a skill that says "expect replies" is argued with.

Then apply the voice rules in [references/mpiv-conventions.md](references/mpiv-conventions.md). The check script flags the banned phrases; the rest is a reread.

## Step 3: fill the folders

- **references/**: one file per topic a step needs in full: the exact template, the query list, the checklist. Each under 300 lines, or with a table of contents.
- **assets/**: files the user copies and fills. Placeholders in curly braces, as in the template. No real names, addresses, or URLs that belong to Michael or a participant.
- **examples/**: the first run, redacted. Timeline with dates, the artifact that worked (the email, the brief, the query), the numbers as a table. Redact people and firms; keep roles, dates, and outcomes.
- **scripts/**: only mechanical work: validating a file, computing a rate, rendering a template. Standard library only, one file, a docstring with the usage line, exit code 1 on failure. A script that does the judgment part of the skill is a sign the skill is not written down yet.
- **evals/evals.json**: two or three prompts a real user would type, one of them an edge case, each with `expected_output` and a list of `expectations` that a grader can check against the output. Format in the guidance file.

## Step 4: check

From the library root:

```
python3 skills/mpiv-skill-creator/scripts/check_skill.py skills/<skill-name>
claude plugin validate .
npx -y skills add . --list
```

The first script checks the frontmatter against the spec, the line count, the provenance block, that every file named in SKILL.md exists, that `evals.json` parses, and that none of the banned phrases appear. The second is Claude Code's own validator. The third proves the skills CLI can see the skill. Fix everything before moving on; a warning from `claude plugin validate` about an unknown field means the field is ignored, so remove it.

## Step 5: run the evals

Run each prompt in `evals/evals.json` twice in fresh subagents, once with the skill path and once without, and grade the expectations against the outputs with evidence for every pass. The official `skill-creator` plugin (`/plugin install skill-creator@claude-plugins-official`) automates the loop and the report; use it when it is installed. Record the pass rate with and without the skill in the changelog. A skill whose expectations pass equally without it is not carrying its weight; cut it down or cut it.

## Step 6: register

1. Add a row to the library `README.md` table: skill name linked to its SKILL.md, one sentence on what it does, and the run it came from.
2. Bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` together. Users on the marketplace path only get updates when the version changes.
3. Add a changelog line in the skill's SKILL.md with the date.
4. Stop. Commit and push are Michael's. Give him the commit command with the author set to `Michael Isaac <michael@mpiv.ai>`.

## Files

- [references/official-guidance.md](references/official-guidance.md): spec and docs rules with sources and check date.
- [references/mpiv-conventions.md](references/mpiv-conventions.md): provenance block, voice rules, exclusions, registration.
- [assets/skill-template/](assets/skill-template/): the SKILL.md, README.md, and evals.json the scaffolder copies.
- [scripts/new_skill.py](scripts/new_skill.py): scaffold a skill folder from the template.
- [scripts/check_skill.py](scripts/check_skill.py): the checks in step 4.
- [evals/evals.json](evals/evals.json): test prompts for this skill.

## Provenance

| Field | Value |
|---|---|
| Origin | Built 2026-09-03 while adding research-first-outreach to the library |
| First run | 2026-09-03: used to add assets, examples, evals, a script, and a provenance block to research-first-outreach |
| Result | Both skills pass `check_skill.py`, `claude plugin validate`, and the skills CLI listing |
| Evidence | c3-consulting-os/research/skill-library-distribution.md; the sources listed in references/official-guidance.md |
| Added to library | 2026-09-03 |

### Changelog

- 2026-09-03: first version.
