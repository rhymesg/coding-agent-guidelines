---
name: skill-writing-guidelines
description: "Use when creating, editing, testing, refining, or reviewing skills."
---

# Skill Writing Guidelines

Write concise skills that people can read and refine. Follow [document-writing-guidelines](../document-writing-guidelines/SKILL.md) for general writing rules.

## General guidelines

- Refer to other skills for applicable instructions and writing conventions.
- Look for ways to work with existing skills. Merge overlapping guidance or refer to its owner instead of duplicating it.
- Check interactions with other skills and instructions: overlapping triggers, conflicting rules, unclear responsibilities, and repeated or recursive workflows.
- Use verb names for skills that perform tasks and `<topic>-guidelines` for rules applied during other tasks.
- Write the description as the trigger: "Use when <situation>", with the words seen at trigger time.
- Write rules as short bullet points and workflows as numbered steps with clear actions and expected results.
- Omit instructions the agent already knows or can infer. Focus on outcomes and leave execution details to the agent's judgment.
- Put general-purpose skills in `coding-agent-guidelines`, generalizing them when appropriate. Keep repository-specific skills in that repository. Symlink each skill into the workspace's skill directory so agents can discover it.

## New skills

- Start with the shortest skill that meets the user's intent and goal.
- Use [review-skill](../review-skill/SKILL.md) for test-driven skill development.

## Editing skills

- Before editing, review the whole structure and workflow. Remove duplicate or unnecessary instructions, combine related points, and reorganize for concision and clarity.
- When the user requests further edits to a skill's output, suggest adding the reusable instruction to the skill for repeatable results.
