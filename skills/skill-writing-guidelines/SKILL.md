---
name: skill-writing-guidelines
description: "Helps write concise, reusable skill instructions. Use when creating, editing, or reviewing a skill."
---

# Skill Writing Guidelines

## General guidelines

### Scope and reuse

- A skill’s instructions apply when the skill is used and its instructions are loaded into context.
- Refer to other skills for applicable instructions and writing conventions.
- Look for ways to work with existing skills. Merge overlapping guidance or refer to its owner instead of duplicating it.
- To apply another skill, write `Use the [skill-name](path/to/SKILL.md) skill for <purpose>.` Keep the instruction in one relevant place.
- Check how the edited skill interacts with other skills and agent instructions.

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
- After creating a skill, use the [review-skill-consistency](../review-skill-consistency/SKILL.md) skill to check it against the other skills and the agent instructions.

## Editing skills

- Before editing, review the whole structure and workflow. Remove duplicate or unnecessary instructions, combine related points, and reorganize for concision and clarity.
