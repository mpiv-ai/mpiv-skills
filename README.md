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

| Skill | What it does |
|---|---|
| [research-first-outreach](skills/research-first-outreach/SKILL.md) | Find independent consultants who publish a repeatable client workflow on their own site, and ask for a 20-minute research conversation in exchange for a written brief. Includes the exact email, list-building prompt, research-page outline, and tracker used in September 2026. |

## How a skill gets in here

A skill is added after it has run on real work at least once and the numbers from that run are in the file. Each skill records where it came from and what happened when it ran.

## License

MIT. Use them, change them, tell me what happened: michael@mpiv.ai.
