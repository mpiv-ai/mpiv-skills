---
name: interview-to-brief
description: Run a research interview and deliver everything promised on it, from a one-workflow interview guide before the call, to a findings file from the transcript, a scroll brief in the participant's own words, a sourced themes memo with named gaps, unlisted hosting, a threaded reply draft, and a promises table tracked to delivery. Use this whenever the user has a research or customer-discovery call booked or done, has a transcript or recording to process, or says "write the interview guide", "process the transcript", "write the brief", "themes memo", "what did I promise", "send the participant what I owe", or "research call follow-up". It is the second half of research-first-outreach.
---

# Interview to brief

This skill takes one research call from the guide written the day before to the reply that carries every promise. On the first run, 2 September 2026, the participant got a brief, a memo with 22 sources, and a packaged method within 30 hours of the call. The reply answered her latest question first.

## What you produce

1. An interview guide with one goal, written before the call.
2. A findings file from the transcript, the same day.
3. A brief: seven scroll slides, her words in the quote block, the workflow table.
4. A themes digest with sources, then a memo written from it.
5. Unlisted pages, a threaded reply draft, a filled delivery table, a register row.

## Step 0: preconditions

- A booked call or a transcript. If the call came from an outreach email, read that email. You owe what it offered.
- The consent frame: research, anonymous by default, no quotes or client names without explicit permission.
- Where findings and candidates live. On the first run: `research/interviews/` and `research/product-candidates.md` in the research repo.
- A recorder. Kept produced the transcript and a processed note on the first run.

## Step 1: the guide, the day before

Fill [assets/interview-guide.md](assets/interview-guide.md) from the participant's website. Put one goal at the top: leave with one recurring workflow described well enough for a one-page brief. Give each section its minutes so 20 minutes stays 20. Keep the guardrails: no pitch, no naming what you are building. The participant agreed to research. Anything else breaks the agreement.

The guide will often name the wrong workflow. The site describes the offer the participant sells. The call shows the chore they run. On the first run the site said parental-leave coverage; the call was about synthesis on a 15-hour week. The second question in the guide ("which chore do you dread most?") surfaced it. When the call goes somewhere else, follow the call.

## Step 2: the findings file, the same day

Fill [assets/findings-template.md](assets/findings-template.md) from the transcript. Sections:

- Guide vs call: what you assumed, what happened, which workflow you are briefing.
- The workflow table: name, trigger, cadence, actors, tools in order, failure without it, what they tried, their words for "fixed". Leave a cell empty when the call did not cover it. Do not fill it from a guess.
- Promises, both sides, in the order made. This list becomes the delivery table.
- Name corrections. Transcripts mangle names and URLs. Check each one on the web before it goes in any file the participant sees. On the first run "Liam Dharmody" and "run doc.io" were Liam Darmody and rundock.ai.
- What stays private: client names they mentioned, anyone they described unkindly.

Add the register row in the same pass. Status `brief` if the workflow table is mostly full. Status `observe` if not.

## Step 3: the brief

Fill [assets/brief-template.html](assets/brief-template.html). Rules:

- The headline and the quote are the participant's words. Copy the quote from the transcript.
- The workflow table repeats the findings table in the second person.
- "What I will go research" lists the themes in the order they came up on the call, each as a question.
- The closing slide names every other promise and when it lands. Check the reply against it later.
- Seven slides or fewer. The reader scrolls on a phone.

## Step 4: the themes digest and the memo

Hand [references/themes-research-prompt.md](references/themes-research-prompt.md) to a background agent as soon as the findings file exists. When it returns, open three of the URLs and confirm the author and date. Then fill [assets/memo-template.html](assets/memo-template.html): what the sources say, a "For you" card that connects the sources to what they said on the call, the sources list, and a Gaps section. The Gaps section says which of their claims nobody has measured. Write it even when it is short.

## Step 5: the writing pass

Run the ban list in `mpiv-skill-creator/scripts/check_skill.py` over every file. Then reread each paragraph and cut any sentence that states a general truth, contrasts two things for effect, or closes a section. The first memo went out with all three and was sent back for a rewrite. Do this before hosting. A hosted file with a shared URL is harder to fix.

## Step 6: host, draft, record

Work through [references/delivery-checklist.md](references/delivery-checklist.md). In short: put the noindex meta tag in each page, copy the pages to the site's unlisted briefs folder with a random filename suffix, commit with the right author, wait for the merge and the deploy, confirm every URL returns 200, then draft the reply in the mailbox as a threaded reply. Answer whatever they asked for last, first. List the promises as a numbered list with links. Close with the next touch and when.

Then fill the Delivery table in the findings file and run:

```
python3 scripts/check_promises.py research/interviews/<date>-<slug>-findings.md
```

It prints every promise not yet Done, Live, or Sent. The call is finished when the script prints zero open rows. Put the remaining rows (aggregated research, quarterly touch) on the calendar.

## Files

Read each file when its step comes up.

- [assets/interview-guide.md](assets/interview-guide.md): the guide with the one-goal frame, minutes, capture checklist, guardrails.
- [assets/findings-template.md](assets/findings-template.md): the findings layout including the promises and delivery sections.
- [assets/brief-template.html](assets/brief-template.html): the seven-slide brief with the MPIV design and placeholders.
- [assets/memo-template.html](assets/memo-template.html): the themes memo page.
- [references/themes-research-prompt.md](references/themes-research-prompt.md): the background-agent prompt and what to check when it returns.
- [references/delivery-checklist.md](references/delivery-checklist.md): checks, hosting, the reply, and the after-send steps.
- [examples/run-2026-09-02.md](examples/run-2026-09-02.md): the first run, redacted: timeline, promises and when each landed, what the guide got wrong, what broke.
- [scripts/check_promises.py](scripts/check_promises.py): lists open rows in the delivery table.
- [evals/evals.json](evals/evals.json): three test prompts with expectations.

## Provenance

| Field | Value |
|---|---|
| Origin | MPIV "AI Workflow Research" interview series, Michael Isaac |
| First run | 2 Sep 2026 call, 42 minutes; deliverables 3 Sep 2026 |
| Result | Guide, findings, brief, digest (22 sources), memo, reply draft, register row; 4 of 7 promises delivered by the next day, 3 scheduled |
| Evidence | c3-consulting-os/research/interviews/2026-09-02-*; [examples/run-2026-09-02.md](examples/run-2026-09-02.md) |
| Added to library | 2026-09-03 |

### Changelog

- 2026-09-03: first version, built from the first run with mpiv-skill-creator. Description reworded for strict YAML. Prose rewritten in plain English.
