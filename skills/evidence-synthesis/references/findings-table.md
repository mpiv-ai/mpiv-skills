# The findings table

## Format

```
| # | Finding | Evidence | Effect on the recommendation |
|---|---|---|---|
| F1 | {One sentence, a claim the client can check} | [S3] {quote or figure}; [S7] {observation} | {What to do differently because this is true} |
```

Source ids come from the inventory (`S1`, `S2`, ...). Every evidence cell has at least one id and the specific thing that id showed: the quote, the figure with its population, the observation with its date.

## Rules

- A finding is one sentence and one claim. Two claims are two rows.
- The evidence cell names the thing, not the source type. "Interview S4: 'nine out of ten requests concern information that already exists'" is evidence. "Interviews" is not.
- The effect cell is an action or a design constraint. "Give employees one knowledge base with a visible owner and review date" is an effect. "Important to consider" is not.
- Claims from one person are cited as one person's claim. Three people saying the same thing is a pattern and the cell says so. A record confirming it makes it a fact.
- An empty evidence cell means the row moves to a "Heard, not confirmed" list below the table. That list is delivered too; it tells the client what to go check.
- Figures carry their population. Two counts of "applications" from two systems are two rows or one row with both counts labeled.

## Rebuilding, not editing

The document is regenerated from the table each time the table changes. Editing the prose directly produces findings the table no longer supports. On the first run the table was rebuilt several times as sources arrived; the deliverable was written from the final table in the last two weeks.

## What a reader checks

A client reads the table by picking three rows and asking to see the evidence. Keep the summaries in the appendix so the check takes minutes.
