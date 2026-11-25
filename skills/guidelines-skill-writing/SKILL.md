---
name: guidelines-skill-writing
description: "Keeps skills and agent instructions short and consistent. Use when creating or editing a skill or the AGENTS.md of the young-agent plugin."
---

# Skill Writing Guidelines

- Name a skill of rules applied during other work `guidelines-<topic>`. Start the name of every other skill with a verb.
- Put a rule in AGENTS.md when most tasks need it and it fits in a few lines; otherwise put it in a skill. Put it in the section whose heading names its topic.
- Start the description with a short sentence on what the skill helps achieve, then a sentence starting "Use when" that states the trigger.
- Start the body directly with rules or workflow: rules as one-clause bullets, workflows as numbered top-level steps with expected results.
- Include only the intent or goal, top-level instructions, rules, and information the agent would not know. Omit detailed commands and sub-steps.
- When rules conflict, prefer dropping one over adding conditions.
- Apply another skill with "Use the [name](path/SKILL.md) skill for <purpose>." instead of repeating its guidance. Name a skill of another plugin as "the <name> skill of the <plugin> plugin", without a path.
