---
name: review-skill-consistency
description: "Finds skills and instructions that conflict, overlap, or leave gaps across every set an agent loads. Use when the user asks to review the skills or instructions of the young-agent plugin, or before a change to them is pushed or merged to main."
---

# Review Skill Consistency

## Workflow

1. Read every instruction file and skill the agent loads: the instruction files and skills of every enabled plugin, personal skills, and the repository's own instruction files and skills.
2. Check the whole set, or a change against it, for the problems below.
3. Use the [guidelines-skill-writing](../guidelines-skill-writing/SKILL.md) skill to develop fixes that keep the whole set consistent.
4. When reviewing a change, open the report with one or two lines on what agents do differently because of it.
5. Report the findings in a table with number, file, problem, and suggested fixes, ordered by importance, at most ten, and only findings that change what an agent does. Do not edit unless asked.

## Problems

- Loading: the coding agent loads the intended instructions and skills, and every referenced skill and file exists.
- Conflicting rules: two rules that cannot both be followed. A skill's rules and workflow steps take precedence over the instruction file's defaults while it runs; this is not a conflict.
- Overlapping triggers: several skills activate for the same request, with unclear responsibility or redundant work.
- Trigger type: the description says whether the agent applies the skill during work or the user invokes it.
- Gaps: work the instructions call for that no skill or rule covers, and references to a missing skill or step.
- Duplicated rules: the same instruction repeated in several places.
- Over-constraint: a rule that forbids or mandates more than needed.
