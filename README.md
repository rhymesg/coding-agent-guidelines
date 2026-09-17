# Coding Agent Guidelines

I use these [guidelines](AGENTS.md) and [skills](skills/) to maintain software quality, keep code maintainable, and make AI-assisted work easy to follow. I value instructions I can read, track in version control, and refine, with clear steps and results I can review.

## Setup

### All projects

Claude Code:

```bash
mkdir -p "$HOME/.claude/skills"
ln -s "$PWD/AGENTS.md" "$HOME/.claude/CLAUDE.md"
ln -s "$PWD"/skills/* "$HOME/.claude/skills/"
```

Codex:

```bash
mkdir -p "$HOME/.codex" "$HOME/.agents/skills"
ln -s "$PWD/AGENTS.md" "$HOME/.codex/AGENTS.md"
ln -s "$PWD"/skills/* "$HOME/.agents/skills/"
```

### One project

Set your project path:

```bash
project="path/to/project"
```

Claude Code:

```bash
mkdir -p "$project/.claude/skills"
ln -s "$PWD/AGENTS.md" "$project/CLAUDE.md"
ln -s "$PWD"/skills/* "$project/.claude/skills/"
```

Codex:

```bash
mkdir -p "$project/.agents/skills"
ln -s "$PWD/AGENTS.md" "$project/AGENTS.md"
ln -s "$PWD"/skills/* "$project/.agents/skills/"
```
