# MPIV skills

The skills MPIsaac Ventures uses in consulting work, published as they are used. Each skill is a folder under `skills/` with a `SKILL.md` that follows the [Agent Skills](https://agentskills.io/specification) format, so it loads in Claude Code and in any other agent that reads the same spec.

## Install

Any agent that supports the skills CLI (Claude Code, Cursor, Codex, Copilot, and others):

```
npx skills add mpiv-ai/mpiv-skills
```

Claude Code, as a plugin with updates:

```
/plugin marketplace add mpiv-ai/mpiv-skills
/plugin install mpiv-skills@mpiv-skills
```

Or copy one folder into `~/.claude/skills/`.

## Skills

| Skill | What it does | Run it came from |
|---|---|---|
| [research-first-outreach](skills/research-first-outreach/SKILL.md) | Find independent consultants who publish a repeatable client workflow on their own site, and ask for a 20-minute research conversation in exchange for a written brief. Includes the exact email, list-building prompt, research-page template, tracker, a redacted run, evals, and a tracker checker. | AI Workflow Research, 20 emails, 31 Aug to 1 Sep 2026 |
| [interview-to-brief](skills/interview-to-brief/SKILL.md) | Run a research interview from the one-goal guide to the reply that carries every promise: findings from the transcript, a scroll brief in the participant's words, a sourced themes memo with named gaps, unlisted hosting, a threaded reply draft, and a promises table checked by a script. | 2026-09-02 call; brief and 22-source memo delivered next day |
| [evidence-synthesis](skills/evidence-synthesis/SKILL.md) | Turn client material into findings a client can check: a source inventory with limits, a findings table with evidence and effect, an evidence-limits section, a client-safe appendix, and an hour ledger against the weekly cap. | Eight-week discovery, June to Aug 2026, 20 hours a week |
| [mpiv-skill-creator](skills/mpiv-skill-creator/SKILL.md) | Turn a method that has run on real work into a new skill here, laid out and checked against the current Agent Skills spec and Claude Code plugin rules, in MPIV's voice, with provenance and evals. | Built and first used 2026-09-03 on research-first-outreach |

## How a skill gets in here

A skill is added after it has run on real work at least once and the numbers from that run are in the file. Each skill records where it came from and what happened when it ran.

## License

MIT. Use them, change them, tell me what happened: michael@mpiv.ai.
