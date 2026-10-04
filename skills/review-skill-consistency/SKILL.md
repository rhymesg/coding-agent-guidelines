---
name: review-skill-consistency
description: "Checks consistency across skills and agent instructions. Use when the user asks to review the skills or the agent instructions as a whole."
---

# Review Skill Consistency

## Workflow

1. Identify and read these two sets:
   - **This skill's source repository:** Read every skill under `skills/`, plus `AGENTS.md` and `CLAUDE.md` where present.
   - **Current environment:** Read every skill the agent can load here, plus all applicable `AGENTS.md` and `CLAUDE.md` files.
   - If the sets contain the same files, review them only once.
2. Check each set for:
   - loading: each agent, such as Claude Code or Codex, loads the intended instructions and skills through imports, symlinks, and copies
   - conflicting rules: two rules that cannot both be followed. A skill's rules and workflow steps take precedence over the `AGENTS.md` defaults while it runs; this is not a conflict.
   - overlapping triggers: multiple skills activate for the same request, with unclear responsibility or redundant work
   - trigger type: the description says whether the agent applies the skill during work or the user invokes it
   - gaps: work the instructions call for that no skill or rule covers, and references to a missing skill or step
   - duplicated rules: the same instruction repeated in multiple places
   - over-constraint: a rule that forbids or mandates more than the owner's style needs
3. Use the [skill-writing-guidelines](../skill-writing-guidelines/SKILL.md) skill to develop fixes that resolve the findings across both sets together, accounting for shared files and checking that each set remains consistent.
   - For a conflict, prefer dropping a rule over adding conditions and specifics.
4. Report the findings without editing, in a table with columns for number, skill/file name, problem, and suggested fix candidates. Order by importance and urgency, and report only the top ten. Report only findings that change what an agent does.
