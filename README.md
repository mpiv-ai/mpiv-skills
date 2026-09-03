# MPIV skills

Skills that MPIsaac Ventures uses in consulting work. Each skill is a folder under `skills/` with a `SKILL.md` in the [Agent Skills](https://agentskills.io/specification) format. It loads in Claude Code and in other agents that read the same format.

## Install

With the skills CLI (Claude Code, Cursor, Codex, Copilot, and others):

```
npx skills add mpiv-ai/mpiv-skills
```

As a Claude Code plugin, with updates:

```
/plugin marketplace add mpiv-ai/mpiv-skills
/plugin install mpiv-skills@mpiv-skills
```

Or copy one folder into `~/.claude/skills/`.

## Skills

| Skill | What it does | Where it came from |
|---|---|---|
| [research-first-outreach](skills/research-first-outreach/SKILL.md) | Find independent consultants who describe a repeatable client process on their own website. Email each one to ask for a 20-minute research conversation in exchange for a written brief. Includes the email, the list-building prompt, the research-page template, the tracker, a redacted run, evals, and a tracker checker. | 20 emails sent 31 Aug and 1 Sep 2026 |
| [interview-to-brief](skills/interview-to-brief/SKILL.md) | Run a research interview and deliver what was promised: the guide, the findings file, the brief, the themes memo, unlisted hosting, the reply draft, and a promises table checked by a script. | One call on 2 Sep 2026; brief and memo delivered the next day |
| [evidence-synthesis](skills/evidence-synthesis/SKILL.md) | Turn client material into findings the client can check: a source inventory with limits, a findings table with evidence and effect, an evidence-limits section, a client-safe appendix, and an hour ledger against the weekly cap. | Eight-week discovery, June to Aug 2026, 20 hours a week |
| [mpiv-skill-creator](skills/mpiv-skill-creator/SKILL.md) | Turn a method that has run on real work into a new skill here. Checks it against the Agent Skills spec and the Claude Code plugin rules. Adds provenance and evals. | Built and first used 3 Sep 2026 |

## How a skill gets in here

A skill is added after the method has run on real work at least once. The numbers from that run go in the file. Each skill records where it came from and what happened when it ran.

## License

MIT. Use them, change them, tell me what happened: michael@mpiv.ai.
