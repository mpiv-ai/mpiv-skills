# research-first-outreach

Find independent consultants who describe a repeatable client process on their own website. Email each one to ask for a 20-minute research conversation in exchange for a written brief. Michael Isaac used this on 31 August and 1 September 2026: 20 emails, one reply within 18 hours, one call the next morning.

Install with the rest of the library: `npx skills add mpiv-ai/mpiv-skills --skill research-first-outreach`, or point Claude at [SKILL.md](SKILL.md).

## What is in here

- `SKILL.md`: the method in seven steps, with the numbers from the run.
- `references/email-template.md`: the email, both variants, the yes reply, the one follow-up.
- `references/list-building.md`: search queries, the checks, record fields, a prompt for an agent.
- `references/research-page.md`: what the research page needs to say.
- `references/tracking.md`: tracker columns and the note logged per send.
- `assets/`: the tracker CSV and the research page HTML, with placeholders.
- `examples/`: the first run, redacted, and the 20 sends by cohort.
- `scripts/check_tracker.py`: checks the tracker and prints reply rate per cohort.
- `evals/evals.json`: three test prompts.

## The one rule

The research has to be real and the brief has to be delivered. Run the interviews only if you would still run them with no chance of a sale.

## License

MIT, with the rest of the [MPIV skill library](../../README.md).
