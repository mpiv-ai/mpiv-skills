# Delivery checklist

Run this the day after the call. Every line is something that went wrong or nearly did on the first run.

## Before writing

1. Verify every name, firm, and URL the transcript mangled. "Liam Dharmody" and "run doc.io" were Liam Darmody and rundock.ai.
2. Confirm which mailbox the reply goes from and that the participant's email is in the thread you will reply to.
3. Confirm the register row: is the workflow briefable (status `brief`) or only heard (`observe`)?

## The files

1. Findings from the transcript, using [assets/findings-template.md](../assets/findings-template.md). Include the promises list from both sides.
2. Brief from [assets/brief-template.html](../assets/brief-template.html). Their words in the quote block, verbatim. Seven slides or fewer.
3. Themes digest from the research agent, then the memo from [assets/memo-template.html](../assets/memo-template.html). Every number with a source and a date. A Gaps section that names what nobody has published.
4. Voice pass on every file: the ban list in `mpiv-skill-creator/scripts/check_skill.py`, then a reread for sentences whose job is to land, contrast, or announce candor. The first memo shipped with all three and was sent back.

## Hosting

Participant pages are unlisted, not private. Put `<meta name="robots" content="noindex, nofollow">` in each file, copy them to `mpiv-main/public/research/briefs/<lastname>-<8 hex chars>.html`, and keep `/research/briefs` in the robots disallow list. Commit as `Michael Isaac <michael@mpiv.ai>`; a different author email fails the Vercel deploy. The URLs return 404 until the PR is merged and deployed, so the reply waits for the merge.

## The reply

A threaded reply draft in the mailbox, never a send. Lead with whatever they asked for in their last email. Then the promises as a numbered list with links. Close on the relationship: the next touch and when.

## After sending

1. Fill the Delivery table in the findings file: promise, artifact, status.
2. Update the register row.
3. Write the memory: who, what they said, what was promised, where the files are.
4. Put the next touch on the calendar. Quarterly was the promise on the first run.
