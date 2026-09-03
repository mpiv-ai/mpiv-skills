# Delivery checklist

Run this the day after the call. Each line comes from something that went wrong or nearly went wrong on the first run.

## Before writing

1. Check every name, firm, and URL the transcript mangled. "Liam Dharmody" and "run doc.io" were Liam Darmody and rundock.ai.
2. Confirm which mailbox the reply goes from, and that the participant's email is in the thread you will reply to.
3. Confirm the register row: `brief` if the workflow is described well enough, `observe` if only heard.

## The files

1. Findings from the transcript, using [assets/findings-template.md](../assets/findings-template.md). Include the promises list from both sides.
2. Brief from [assets/brief-template.html](../assets/brief-template.html). Their words in the quote block, copied from the transcript. Seven slides or fewer.
3. Themes digest from the research agent, then the memo from [assets/memo-template.html](../assets/memo-template.html). Every number with a source and a date. A Gaps section that names what nobody has published.
4. Writing pass on every file: the ban list in `mpiv-skill-creator/scripts/check_skill.py`, then a reread that cuts general truths, contrast pairs, and closing lines. The first memo shipped with all three and was sent back.

## Hosting

Participant pages are unlisted. Put `<meta name="robots" content="noindex, nofollow">` in each file. Copy them to `mpiv-main/public/research/briefs/<lastname>-<8 hex chars>.html`. Keep `/research/briefs` in the robots disallow list. Commit as `Michael Isaac <michael@mpiv.ai>`. A different author email fails the Vercel deploy. The URLs return 404 until the PR is merged and deployed. Send the reply after that.

## The reply

A threaded reply draft in the mailbox. Never send. Answer whatever they asked for in their last email first. Then the promises as a numbered list with links. End with the next touch and when.

## After sending

1. Fill the Delivery table in the findings file: promise, artifact, status.
2. Update the register row.
3. Write the memory: who, what they said, what was promised, where the files are.
4. Put the next touch on the calendar. On the first run the promise was quarterly.
