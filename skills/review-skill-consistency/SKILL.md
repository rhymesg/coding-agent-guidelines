---
name: review-skill-consistency
description: "Checks consistency across skills and agent instructions. Use when the user asks to review the skills or the agent instructions as a whole."
---

# Review Skill Consistency

## Workflow

1. Identify and read these two sets:
   - **This skill's source repository:** Read every skill under `skills/`, plus `AGENTS.md` and `CLAUDE.md`.
   - **Current environment:** Read every skill the agent can load here, plus all applicable `AGENTS.md` and `CLAUDE.md` files.
   - If the sets contain the same files, review them only once.
2. Check each set for:
   - conflicting rules: two rules that cannot both be followed. When the user requests a skill, its workflow steps count as part of that request.
   - overlapping triggers: multiple skills activate for the same request, with unclear responsibility or redundant work
   - excessive activation: triggers or workflow calls that invoke a skill more often, or for smaller tasks, than needed
   - gaps: work the instructions call for that no skill or rule covers, and references to a missing skill or step
   - duplicated rules: the same instruction repeated in multiple places
3. Use the [skill-writing-guidelines](../skill-writing-guidelines/SKILL.md) skill to develop fixes that resolve the findings across both sets together, accounting for shared files and checking that each set remains consistent.
4. Report the findings without editing, in a table with columns for skill/file name, problem, and suggested fix candidates.
