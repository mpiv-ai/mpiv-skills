# research-first-outreach

A Claude skill for finding people who publish how they work, and asking them for a 20-minute research conversation instead of pitching them. This is the method Michael Isaac used to reach 20 independent consultants cold in September 2026, one of whom booked a call inside 18 hours.

## Install

With the skills CLI:

```
npx skills add mpiv-ai/mpiv-skills --skill research-first-outreach
```

Or tell Claude:

> Read https://raw.githubusercontent.com/mpiv-ai/mpiv-skills/main/skills/research-first-outreach/SKILL.md and set this up for me. Start with step 0.

Or copy this folder to `~/.claude/skills/research-first-outreach/`.

## What is in here

- `SKILL.md`: the method, seven steps, plus the numbers from the run.
- `references/email-template.md`: the exact email, both variants, the "yes" reply, the one follow-up.
- `references/list-building.md`: search queries, the qualification checklist, record fields, a prompt you can hand an agent.
- `references/research-page.md`: what the public research page needs to say.
- `references/tracking.md`: tracker columns and the note logged per send.

## The one rule

The research has to be real and the brief has to be delivered. Run the interviews only if you would still run them with zero chance of a sale.

## License

MIT, with the rest of the [MPIV skill library](../../README.md).
