# The themes research prompt

Hand this to a background agent (Sonnet is enough) the same day as the call. It produces the sourced digest the memo is written from. Fill the braces; keep the rules.

```
Objective: produce a sourced research digest on {N} themes from a customer-discovery interview with {role, no name}. The digest feeds a short memo Michael Isaac will send to the interviewee. Write it to {path}/research/interviews/{date}-{slug}-themes-research.md.

Use web search and read the actual pages. Aim for 4 to 8 credible sources per theme from 2024 to 2026: practitioner blogs, Substacks, podcast transcripts, surveys, reports, community threads, vendor research. Prefer primary sources over listicles. Record the exact URL, title, author, date, and a one-line quote or paraphrase per source. Do not invent sources. If you cannot find evidence for a theme, say so in the file.

The themes:

1. {Theme}. {Two or three sentences of what the interviewee said, without naming them.} Questions: {two or three}.
2. {Theme}. ...

File format: Markdown. H1 title, a two-line provenance header (date, method, tools). One H2 per theme. Under each: a "What the sources say" paragraph or two of plain synthesis, then a "Sources" list, one bullet per source: [Title](URL), author, date, one-line takeaway. Close with an H2 "Gaps" listing what you could not find. No em dashes. No flourish words. Under 1800 words.

Exclusions: write nothing else in the repo. Do not name the interviewee or their clients. Do not commit.

Report back: the file path, word count, sources per theme, and any theme where evidence was thin.
```

What to check when it returns: open three of the URLs at random and confirm the author and date. A digest with an invented source is worse than none.
