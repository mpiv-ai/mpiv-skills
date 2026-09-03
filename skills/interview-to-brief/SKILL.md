---
name: interview-to-brief
description: Run a research interview and deliver everything promised on it: a one-workflow interview guide before the call, a findings file from the transcript, a scroll brief in the participant's own words, a sourced themes memo with named gaps, unlisted hosting, a threaded reply draft, and a promises table tracked to delivery. Use this whenever the user has a research or customer-discovery call booked or done, has a transcript or recording to process, or says "write the interview guide", "process the transcript", "write the brief", "themes memo", "what did I promise", "send the participant what I owe", or "research call follow-up". It is the second half of research-first-outreach.
---

# Interview to brief

A research call is worth what reaches the participant afterward. This skill takes one call from the guide written the day before to the reply that carries every promise, with the files and checks from the first run attached. On that run the participant got a brief, a memo with 22 sources, and a packaged method inside 30 hours of the call, and the fastest thing she asked for came first in the reply.

The method works because the guide has one goal, the brief uses their words, the memo names what nobody has published, and the promises are written down before the reply is drafted.

## What you produce

1. An interview guide with one goal, before the call.
2. A findings file from the transcript, the same day.
3. A brief: seven scroll slides, their verbatim quote, the workflow table.
4. A themes digest with sources, then a memo written from it.
5. Unlisted pages, a threaded reply draft, a filled delivery table, a register row.

## Step 0: preconditions

- A booked call or a transcript. If the call came from an outreach email, read that email: what was offered is what is owed.
- The consent frame: research, anonymous by default, no quotes or client names without explicit permission.
- Where findings and candidates live. On the first run: `research/interviews/` and `research/product-candidates.md` in the research repo.
- A recorder. Kept produced the transcript and a processed note on the first run.

## Step 1: the guide, the day before

Fill [assets/interview-guide.md](assets/interview-guide.md) from their website. One goal at the top: leave with one recurring workflow described well enough for a one-page brief. Minutes per section, so 20 minutes stays 20. The guardrails say no pitch and no naming what you are building, because the participant agreed to research and will hear anything else as the bait switching.

Expect the guide to be wrong about which workflow matters. Their site describes the offer they sell; the call reveals the chore they run. The second question in the guide exists to surface that. Follow the call, not the guide.

## Step 2: the findings file, the same day

Fill [assets/findings-template.md](assets/findings-template.md) from the transcript. The sections that earn their place:

- Guide vs call: what you assumed, what happened, which workflow you are briefing.
- The workflow table: name, trigger, cadence, actors, tools in order, failure without it, what they tried, their words for "fixed". Empty cells are information; do not fill them from guesswork.
- Promises, both sides, in the order made. This list becomes the delivery table.
- Name corrections. Transcripts mangle names and URLs; verify each against the web before it reaches any file the participant sees.
- What stays private: client names they mentioned, anyone they described unkindly.

Add the register row in the same pass: status `brief` if the workflow table is mostly full, `observe` if not.

## Step 3: the brief

Fill [assets/brief-template.html](assets/brief-template.html). Rules from the first run:

- The headline and the quote are their words. Pull the quote verbatim from the transcript.
- The workflow table repeats the findings table in the second person.
- "What I will go research" lists the themes in the order they came up on the call, each as a question.
- The closing slide names every other promise and when it lands. It is the contract the reply will be checked against.
- Seven slides or fewer. The reader scrolls on a phone.

## Step 4: the themes digest and the memo

Hand [references/themes-research-prompt.md](references/themes-research-prompt.md) to a background agent as soon as the findings file exists. When it returns, spot-check three URLs. Then fill [assets/memo-template.html](assets/memo-template.html): what the sources say, a "For you" card that connects the sources to what they said, the sources list, and a Gaps section. The Gaps section is the part participants trust; it says which of their own claims nobody has measured.

## Step 5: the voice pass

Run the ban list in `mpiv-skill-creator/scripts/check_skill.py` over every file, then reread each paragraph and cut any sentence whose job is to land, contrast, or announce candor. The first memo went out with all three and came back. Do this before hosting, because a hosted file with a shared URL is harder to fix quietly.

## Step 6: host, draft, record

Work through [references/delivery-checklist.md](references/delivery-checklist.md). In short: noindex meta in each page, copy to the site's unlisted briefs folder with an unguessable filename, commit with the right author, wait for the merge and the deploy, verify every URL returns 200, then draft the reply in the mailbox as a threaded reply. Lead with whatever they asked for last. Promises as a numbered list with links. Close on the next touch.

Then fill the Delivery table in the findings file and run:

```
python3 scripts/check_promises.py research/interviews/<date>-<slug>-findings.md
```

It prints every promise not yet Done, Live, or Sent. Zero open rows is the definition of finished for this call. The remaining rows (aggregated research, quarterly touch) go on the calendar.

## Files

Read these when the step calls for them, not up front.

- [assets/interview-guide.md](assets/interview-guide.md): the guide with the one-goal frame, minutes, capture checklist, guardrails.
- [assets/findings-template.md](assets/findings-template.md): the findings layout including the promises and delivery sections.
- [assets/brief-template.html](assets/brief-template.html): the seven-slide brief with the MPIV design and placeholders.
- [assets/memo-template.html](assets/memo-template.html): the themes memo page.
- [references/themes-research-prompt.md](references/themes-research-prompt.md): the background-agent prompt and what to check when it returns.
- [references/delivery-checklist.md](references/delivery-checklist.md): verification, hosting, the reply, and the after-send steps.
- [examples/run-2026-09-02.md](examples/run-2026-09-02.md): the first run, redacted: timeline, promises and when each landed, what the guide got wrong, what broke.
- [scripts/check_promises.py](scripts/check_promises.py): lists open rows in the delivery table.
- [evals/evals.json](evals/evals.json): three test prompts with expectations.

## Provenance

| Field | Value |
|---|---|
| Origin | MPIV "AI Workflow Research" interview series, Michael Isaac |
| First run | 2026-09-02 call, 42 minutes; deliverables 2026-09-03 |
| Result | Guide, findings, brief, digest (22 sources), memo, reply draft, register row; 4 of 7 promises delivered by the next day, 3 scheduled |
| Evidence | c3-consulting-os/research/interviews/2026-09-02-*; [examples/run-2026-09-02.md](examples/run-2026-09-02.md) |
| Added to library | 2026-09-03 |

### Changelog

- 2026-09-03: first version, built from the first run with mpiv-skill-creator.
