---
name: evidence-synthesis
description: Turn a pile of client material (call transcripts, Notion, Slack, Drive exports, registries) into a findings document where every finding has evidence and an effect, every source has a stated limit, and the work fits a weekly hour cap. Use this whenever the user is on a part-time or fractional engagement and says "synthesize", "pull this together", "what are the findings", "current state", "discovery", "evidence appendix", "what does the material say", "I have 80 documents and 15 hours", or asks how to keep a client synthesis inside a fixed budget. Also use it to check an existing findings document for findings without evidence.
---

# Evidence synthesis

The deliverable is a set of findings the client can check. Each finding cites its source and says what it changes in the recommendation. A separate section says where the evidence stops. The first run was an eight-week discovery for a remote company on a 20-hour-a-week cap, with some weeks authorized to 30. Sources: thirteen interviews, two tool registries that counted different populations, a sampled Notion review, five published peer practices, and three vendor sessions. Output: five deliverables and four appendices. Raw transcripts were excluded. Client-safe summaries went in their place.

The work runs in passes. Each pass adds finding candidates and source pointers to one persistent project for the client. The document is rebuilt from the findings table each time the table changes.

## What you produce

1. A source inventory: every source with what it covered, its limit, and a count.
2. A findings table: finding, evidence with source ids, effect on the recommendation.
3. An evidence-limits section: where the evidence stops.
4. A client-safe appendix: summaries of interviews and reviews, no raw transcripts.
5. An hour ledger against the cap.

## Step 0: the budget and the date

Write down the weekly cap, any authorized overage, the deliverable date, and what the client already treats as true (a registry, a decision log, a dashboard). Split the weeks into passes. On the first run: 20 hours a week, 30 when authorized, eight weeks, deliverables written in the last two.

## Step 1: inventory before reading

Fill [assets/source-inventory.csv](assets/source-inventory.csv) before reading anything for content. One row per source: id, name, type, how it comes in (MCP, export, transcript, interview), what it covers, its limit, a count, and dates. Fill the limit column on day one. Examples of limits: "The registry lists tools the company knows about. Discovery observed tools used with company email. The two count different populations." "The requested export was not received." Update the column when a source arrives or fails to arrive.

## Step 2: one persistent project per client, intake in a fixed order

Put everything for the client in one persistent project so context carries across sessions. Intake order, with details in [references/intake-order.md](references/intake-order.md):

1. Records and decisions: registries, decision logs, objective pages, policies. The client already treats these as true.
2. Interviews: transcripts, one per session, summarized to a client-safe note the same day.
3. Chat and working docs: Slack, Drive, working Notion pages. Read these to confirm or contradict candidates from steps 1 and 2.

On the first run most material came in through MCP connections to the client's workspace, plus call transcripts. An MCP read is current on the day you read it. An export is stale from the day it was made. Record the date of each in the inventory.

## Step 3: extraction passes

Each pass reads one slice of the inventory and adds rows to a candidates list: a one-line finding candidate, the source id, the quote or figure, and a confidence note. Do not write prose yet. On the first run sources arrived over six weeks and the table was rebuilt several times.

Rules from the first run:

- A figure carries the population it measures. "153 applications in the registry" and "839 applications observed by discovery" are two facts. The table says which is which.
- One person's claim is cited as one person's claim. Three people saying the same thing is a pattern. A record confirming it makes it a fact.
- Anything unkind about a named person stays out of every file the client sees.

## Step 4: the findings table

Fill [assets/findings-table.md](assets/findings-table.md): finding, evidence (source ids plus the quote, figure, or observation), effect on the recommendation. Format and rules in [references/findings-table.md](references/findings-table.md). If the evidence cell is empty, delete the row or move it to the "Heard, not confirmed" list. The effect cell says what the client should do differently because the finding is true.

## Step 5: where the evidence stops

Write the evidence-limits section from the inventory's limit column: which sources were samples, which never arrived, which counts measure different things, and what the figures do and do not show. Sentence patterns in [assets/evidence-limits.md](assets/evidence-limits.md). This section stops the findings from being stretched later.

## Step 6: the client-safe appendix

Turn each interview and review into a short summary: function, what they described, the finding candidates it supported. Exclude raw transcripts from the deliverable. Say so in the evidence-used table.

## Step 7: the ledger and the check

Log hours per week in [assets/hour-ledger.csv](assets/hour-ledger.csv) against the cap. Then run:

```
python3 scripts/check_evidence.py assets/source-inventory.csv assets/findings-table.md assets/hour-ledger.csv
```

It fails when a finding cites no source, when a finding cites an id missing from the inventory, when an inventory source is never cited, or when a week exceeds its cap. Run it before every draft the client sees.

## Files

Read each file when its step comes up.

- [references/intake-order.md](references/intake-order.md): the order, the reasons, and how MCP reads, exports, and transcripts differ.
- [references/findings-table.md](references/findings-table.md): the table format, the evidence rules, the effect column.
- [assets/source-inventory.csv](assets/source-inventory.csv): the inventory columns with one example row.
- [assets/findings-table.md](assets/findings-table.md): the table template with source-id citations.
- [assets/evidence-limits.md](assets/evidence-limits.md): sentence patterns for the limits section.
- [assets/hour-ledger.csv](assets/hour-ledger.csv): weekly hours against the cap.
- [examples/run-2026-06.md](examples/run-2026-06.md): the first run, redacted: sources, passes, what arrived late, what was excluded, the hours.
- [scripts/check_evidence.py](scripts/check_evidence.py): the citation and cap check.
- [evals/evals.json](evals/evals.json): three test prompts with expectations.

## Provenance

| Field | Value |
|---|---|
| Origin | MPIV discovery engagement for a remote consumer-tech company, through a talent marketplace, June to August 2026 |
| First run | Eight weeks, 20 hours a week with some weeks authorized to 30; 13 interviews, 2 registries, a sampled workspace review, 5 peer practices, 3 vendor sessions |
| Result | Final handover 4 Aug 2026: five deliverables and four appendices, each finding with evidence and effect, an evidence-limits section, raw transcripts excluded |
| Evidence | The handover set in the MPIV archive; [examples/run-2026-06.md](examples/run-2026-06.md) |
| Added to library | 2026-09-03 |

### Changelog

- 2026-09-03: first version, built with mpiv-skill-creator from the June to August 2026 run and the 2 September 2026 research interview that named the hour-cap constraint. Prose rewritten in plain English the same day.
