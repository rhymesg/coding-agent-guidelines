---
name: review-skills
description: "Keeps the skills and the agent instructions working together as one set. Use when the user asks to review the skills or the agent instructions as a whole."
---

# Review Skills

## Workflow

1. Read every skill the agent can load in the current workspace, and the instruction files: `AGENTS.md`, `CLAUDE.md`, and the files they import.
2. Check the set for:
   - conflicting rules
   - overlapping triggers
   - gaps: work the instructions call for that no skill or rule covers, and references to a missing skill or step
   - duplicated rules
3. Report the findings without editing. For each finding, give the files involved, the problem, and a suggested fix based on the [skill-writing-guidelines](../skill-writing-guidelines/SKILL.md) skill.

## Rules

- A skill's own steps are the user's request that wins "unless asked".
- A conflict means two rules can't both be followed.
- A gap means nothing covers the work.
- Duplication means rules that must change together.
