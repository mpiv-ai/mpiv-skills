# Official guidance, checked 2026-09-03

Every rule below has a source. If this file is more than a month old, re-fetch the sources before relying on it. Sources: the Agent Skills specification (https://agentskills.io/specification), the Claude Code skills page (https://code.claude.com/docs/en/skills), the plugins page (https://code.claude.com/docs/en/plugins), the plugin marketplaces page (https://code.claude.com/docs/en/plugin-marketplaces), the eval guide (https://agentskills.io/skill-creation/evaluating-skills), and the skills CLI README (https://github.com/vercel-labs/skills).

## Frontmatter: the spec's six fields

| Field | Required | Rule |
|---|---|---|
| `name` | Yes | 64 chars max, lowercase letters, digits, hyphens; no leading, trailing, or double hyphen; must equal the directory name |
| `description` | Yes | 1024 chars max, non-empty, says what the skill does and when to use it |
| `license` | No | License name or a reference to a bundled file |
| `compatibility` | No | 500 chars max, environment requirements |
| `metadata` | No | String-to-string map for your own tooling |
| `allowed-tools` | No | Space-separated pre-approved tools; experimental in the spec |

Claude.ai uploads, the Skills API, and `package_skill.py` reject any other field with "Unexpected key(s) in SKILL.md frontmatter". A skill that uses only these six fields loads everywhere.

## Claude Code extensions (Claude Code only)

Use these only when the behavior is needed. Other tools reject them.

- `disable-model-invocation: true`: only the user can invoke. For side-effect workflows (send, deploy, publish). The description is not loaded into context; the full skill loads on `/name`.
- `user-invocable: false`: only Claude can invoke. For background knowledge. Description always in context.
- `allowed-tools`, `disallowed-tools`: per-turn grants or removals; clear on the next user message. Pattern for a bundled script: `allowed-tools: Bash(${CLAUDE_SKILL_DIR}/scripts/render.sh *)` and call the script with the same variable in the body.
- `model`, `context: fork`, `agent`, `background`: run in a subagent, choose its model.
- `arguments` plus `$ARGUMENTS`, `$0`, `$1`, and named `$name` placeholders.
- `paths`: restrict the skill to files under given paths.

Keep `name` and `description` free of `: ` (colon plus space) unless the whole value is quoted. Claude Code's validator accepted an unquoted description with a colon on 2026-09-03; the skills CLI silently skipped that skill, because strict YAML reads `: ` as a nested mapping.

Frontmatter is read only when the opening `---` is the first line of the file. Malformed YAML loads the body with empty metadata, so the skill never triggers automatically.

## Size and loading

- Keep SKILL.md under 500 lines; move detail to supporting files and reference them from SKILL.md with a line saying when to read each.
- The skill listing (names plus descriptions) has a context budget of 1 percent of the model window; each entry is capped at 1,536 characters; when the listing overflows, Claude Code drops descriptions from the least-used skills first. Put the key use case first in the description.
- When a skill fires, its rendered SKILL.md enters the conversation once and stays; Claude Code does not re-read it on later turns.

## Command names

- Personal or project skill: the directory name is the command; `name` is only a display label.
- Plugin skill at `plugin/skills/<dir>/SKILL.md`: `/plugin-name:<dir>`, or `/plugin-name:<name>` when the frontmatter sets `name`.

## Plugin and marketplace layout

- Only `plugin.json` lives inside `.claude-plugin/`. `skills/`, `agents/`, `hooks/`, `scripts/` sit at the plugin root.
- `plugin.json` fields: `name` (required), `description`, `version`, `author`, `homepage`, `repository`, `license`, `keywords`, and component paths such as `"skills": "./skills"`. Users on the marketplace path receive updates only when `version` changes.
- `marketplace.json` at the repo root: `name`, `owner.name` (required), `plugins[]` with `name` and `source`. `source: "./"` makes the repo root the plugin. `metadata` accepts `description` and `version`; `claude plugin validate` warns on unknown keys such as `metadata.repository`.
- Add with `/plugin marketplace add owner/repo`, install with `/plugin install <plugin>@<marketplace>`, reload with `/reload-plugins`. Test without installing: `claude --plugin-dir ./path`.
- Validate: `claude plugin validate ./path` (also accepts a bare skills directory). `--strict` turns warnings into errors. The community marketplace runs the same check on submission.

## The skills CLI

`npx skills add owner/repo` installs every skill it finds; `--list` shows them; `--skill <name>` installs one. It walks `SKILL.md` at the root, `skills/<name>/SKILL.md`, and catalog layouts up to two category levels. Local paths work: `npx -y skills add . --list`. It writes to the directory convention of 70-plus agents, so a repo in this layout reaches Cursor, Codex, Copilot, and the rest without changes.

## Evals

Documented format, `evals/evals.json` inside the skill directory:

```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "A realistic user message",
      "expected_output": "What success looks like, in a sentence",
      "files": ["evals/files/input.csv"],
      "expectations": ["A verifiable statement about the output"]
    }
  ]
}
```

Rules from the eval guide: start with 2 to 3 cases; vary the phrasing; include one edge case; write expectations after seeing the first outputs; expectations must be checkable from the output ("the chart has labeled axes"), not opinions ("the output is good"); grade each with evidence; run with the skill and without it in fresh contexts and compare pass rate, time, and tokens. The official `skill-creator` plugin (`/plugin install skill-creator@claude-plugins-official`) runs this loop and produces the report. `claude plugin eval` (case.yaml under `evals/`) exists but is marked early access as of 2026-09-03 and its `init --bare` wrote nothing on this machine; prefer `evals.json` until that changes.

## Supporting files, from the docs

```
my-skill/
├── SKILL.md        (required: overview and navigation)
├── reference.md    (loaded when needed)
├── examples.md     (loaded when needed)
└── scripts/
    └── helper.py   (executed, not loaded)
```

Scripts are executed, not read, so they use no context. Bundle a script when every run would otherwise write the same helper. Keep scripts to mechanical work.
