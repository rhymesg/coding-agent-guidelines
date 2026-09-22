---
name: skill-writing-guidelines
description: "Helps write concise, reusable skill instructions. Use when creating, editing, or reviewing skills, AGENTS.md, or CLAUDE.md."
---

# Skill Writing Guidelines

## General guidelines

- The rules for a skill body also apply to `AGENTS.md` and `CLAUDE.md`.

### Scope and reuse

- Refer to other skills for applicable instructions and writing conventions.
- Look for ways to work with existing skills. Merge overlapping guidance or refer to its owner instead of duplicating it.
- To apply another skill, write `Use the [skill-name](path/to/SKILL.md) skill for <purpose>.` Keep the instruction in one relevant place.
- Check interactions with other skills and instructions: overlapping triggers, conflicting rules, unclear responsibilities, and repeated or recursive workflows.

### Naming and placement

- Use verb names for skills that perform tasks and `<topic>-guidelines` for rules applied during other tasks.
- Put general-purpose skills in `coding-agent-guidelines`, generalizing them when appropriate. Keep repository-specific skills in that repository. Symlink each skill into the workspace's skill directory so agents can discover it.

### Description and body

- Start the description with a short sentence describing what the skill helps achieve; avoid merely restating its name. Use a second sentence beginning "Use when" to state the trigger.
- Start the body directly with guidelines or workflow; omit an opening sentence explaining the skill.
- Write rules as short bullet points and workflows as numbered steps with clear actions and expected results.
- Omit instructions the agent already knows or can infer. Focus on outcomes and leave execution details to the agent's judgment.

## New skills

- Start with the shortest skill that meets the user's intent and goal.

## Editing skills

- Before editing, review the whole structure and workflow. Remove duplicate or unnecessary instructions, combine related points, and reorganize for concision and clarity.
- When the user requests further edits to a skill's output, suggest adding the reusable instruction to the skill for repeatable results.
