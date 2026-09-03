---
name: {skill-name}
description: {What the skill produces, in one clause. Then the phrases a user says that should trigger it: "...", "...", "...". Then the contexts. Under 1024 characters.}
---

# {Skill title}

{One paragraph: what this produces, where the method came from, and why it works. Include the number from the first run.}

## What you produce

1. {Artifact one}
2. {Artifact two}

## Step 0: preconditions

{What must be true before starting. Ask the user for what is missing.}

## Step 1: {first step}

{Instructions with the reason behind each rule.}

## Step 2: {next step}

## Files

Read these when the step calls for them, not up front.

- [references/{topic}.md](references/{topic}.md): {what it holds and when to open it}.
- [assets/{file}](assets/{file}): {the template the user copies}.
- [examples/{run}.md](examples/{run}.md): {the redacted first run}.
- [scripts/{check}.py](scripts/{check}.py): {the mechanical check and the command}.
- [evals/evals.json](evals/evals.json): test prompts with expectations.

## Provenance

| Field | Value |
|---|---|
| Origin | {campaign, engagement, person, date} |
| First run | {date and scale, or "none yet"} |
| Result | {the numbers} |
| Evidence | {where the proof lives} |
| Added to library | {YYYY-MM-DD} |

### Changelog

- {YYYY-MM-DD}: first version.
