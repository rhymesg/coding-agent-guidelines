# Coding Agent Guidelines

This repository contains [guidelines](AGENTS.md) and [skills](skills/) for personal use.

I value instructions I can read and refine, with clear steps and results I can review. These instructions evolve as the models evolve.

## Quotes

> Code is cheap. Quality is not. The job of a software engineer has never really been about putting lines of code on the screen. It's been about architecting elegant solutions to complex problems, thinking 10 steps ahead about how a system will evolve, and retaining flexibility in the face of changing requirements.

*— Jonathan Kelley, Dioxus — AI Engineer World's Fair, July 2026*

> Intelligence is the ability to solve a problem. Now, in a world where intelligence has become very cheap and abundant, you can solve anything. What's the bottleneck? The bottleneck becomes the question: "Okay, what do I want to solve?" I can have anything I want. What do I want?

*— Yuval Noah Harari — EDP 50th Anniversary Gala Dinner, July 2026*

## Setup

Symlink the guidelines to follow them as they are. To add your own rules, import them inline instead.

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

### Import inline

Append this in your `CLAUDE.md` or `AGENTS.md`:

```
@path/to/coding-agent-guidelines/AGENTS.md
```
