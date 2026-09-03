---
name: evidence-synthesis
description: Turn a pile of client material (call transcripts, Notion, Slack, Drive exports, registries) into a findings document where every finding has evidence and an effect, every source has a stated limit, and the work fits a weekly hour cap. Use this whenever the user is on a part-time or fractional engagement and says "synthesize", "pull this together", "what are the findings", "current state", "discovery", "evidence appendix", "what does the material say", "I have 80 documents and 15 hours", or asks how to keep a client synthesis inside a fixed budget. Also use it to check an existing findings document for findings without evidence.
---

# Evidence synthesis

The deliverable is a set of findings a client can check. Each finding cites the source it came from, says what it changes in the recommendation, and sits next to a statement of where the evidence stops. The first run was an eight-week discovery for a remote company, on a 20-hour-a-week cap with some weeks authorized to 30: thirteen interviews, two tool registries that counted different populations, a sampled Notion review, five peer practices, and three vendor sessions became five deliverables and four appendices, with raw transcripts excluded and client-safe summaries in their place.

The method works because the inventory comes before the reading, the intake runs in a fixed order, the findings table has an evidence cell that cannot be left blank, and the hours are counted every week against the cap. It runs incrementally: each pass adds finding candidates and evidence pointers to a persistent project for the client, and the document is rebuilt from the table, never edited by hand into shape.

## What you produce

1. A source inventory: every source with what it covered, its limit, and a count.
2. A findings table: finding, evidence with source ids, effect on the recommendation.
3. An evidence-limits section: where the evidence stops, in plain sentences.
4. A client-safe appendix: summaries of interviews and reviews, no raw transcripts.
5. An hour ledger against the cap.

## Step 0: the budget and the date

Write down the weekly cap, any authorized overage, the deliverable date, and what the client already trusts (a registry, a decision log, a dashboard). Divide the weeks into passes. On the first run: 20 hours a week, 30 when authorized, eight weeks, deliverables in the last two. A synthesis with no cap written down expands to fill the material.

## Step 1: inventory before reading

Fill [assets/source-inventory.csv](assets/source-inventory.csv) before opening anything for content. One row per source: id, name, type, how it comes in (MCP, export, transcript, interview), what it covers, its limit, a count. The limit column is the one people skip and the one the client reads. "The registry lists tools the company knows about; discovery observed tools used with company email; they measure different populations" is a limit. "The requested export was not received" is a limit. Write those on day one and update them when a source arrives or fails to.

## Step 2: one persistent project per client, intake in a fixed order

Everything for the client goes into one persistent project so context is not rebuilt each session. Intake order, and why, in [references/intake-order.md](references/intake-order.md):

1. Records and decisions first: registries, decision logs, OKR pages, policies. These are what the client already treats as true.
2. Interviews second: transcripts, one per session, summarized to a client-safe note the same day.
3. Chat and working docs last: Slack, Drive, working Notion pages. These are wide and shallow; read them to confirm or contradict, not to discover.

On the first run most material came in through MCP connections to the client's workspace plus call transcripts. Live MCP reads mean the working set stays current; exports go stale the day they are made, so mark each export with its date in the inventory.

## Step 3: extraction passes

Each pass reads one slice of the inventory and adds rows to a candidates list: a one-line finding candidate, the source id, the quote or figure, and a confidence note. Do not write prose yet. The passes are incremental on purpose; the first run's findings were rebuilt several times as sources arrived, and a table absorbs that where a draft does not.

Rules that held on the first run:

- A figure travels with the population it measures. "153 applications in the registry" and "839 applications observed by discovery" are two facts, not a contradiction, and the table says which is which.
- One person's claim is a claim, cited as such. Three people's agreement is a pattern. Neither is a fact until a record confirms it.
- Anything unkind about a named person stays out of every file the client sees.

## Step 4: the findings table

Fill [assets/findings-table.md](assets/findings-table.md): finding, evidence (source ids and the specific quote, figure, or observation), effect on the recommendation. Format and rules in [references/findings-table.md](references/findings-table.md). A finding with an empty evidence cell is deleted or moved to a "heard, not confirmed" list. The effect cell is what makes the table a deliverable rather than notes: it says what the client should do differently because this is true.

## Step 5: where the evidence stops

Write the evidence-limits section from the inventory's limit column: which sources were samples, which never arrived, which counts measure different things, and what the figures therefore do and do not show. Pattern sentences in [assets/evidence-limits.md](assets/evidence-limits.md). Clients trust the document more when it names its own edges, and the section protects the recommendation from being stretched later.

## Step 6: the client-safe appendix

Interviews and reviews become short summaries: function, what they described, the finding candidates it supported. Raw transcripts are excluded from the deliverable. Say so in the evidence-used table.

## Step 7: the ledger and the check

Log hours per week in [assets/hour-ledger.csv](assets/hour-ledger.csv) against the cap. Then run:

```
python3 scripts/check_evidence.py assets/source-inventory.csv assets/findings-table.md assets/hour-ledger.csv
```

It fails when a finding cites no source, cites a source id missing from the inventory, when an inventory source is never cited, or when a week exceeds its cap. Run it before every draft the client sees.

## Files

Read these when the step calls for them, not up front.

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
| Result | Final handover 2026-08-04: five deliverables and four appendices, each finding with evidence and effect, an evidence-limits section, raw transcripts excluded |
| Evidence | The handover set in the MPIV archive; [examples/run-2026-06.md](examples/run-2026-06.md) |
| Added to library | 2026-09-03 |

### Changelog

- 2026-09-03: first version, built with mpiv-skill-creator from the June to August 2026 run and the 2026-09-02 research interview that named the hour-cap constraint.
