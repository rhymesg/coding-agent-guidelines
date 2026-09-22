---
name: refine-skill
description: "Refines skill instructions through testing and feedback. Use when the user asks to refine, review, or clean up a skill."
disable-model-invocation: true
---

# Refine Skill

## Test-driven skill development

**Setup**

1. Clarify the user's intent and agree on what a successful result should look like.
2. Look for existing outputs. If available, confirm with the user which represent the desired result and use them as references.

**Repeat until the user confirms that the output matches their intent:**

1. Use the [skill-writing-guidelines](../skill-writing-guidelines/SKILL.md) skill to review the instructions and revise as needed: add missing guidance, clarify or shorten instructions, or remove unnecessary content.
2. Perform a representative task using the skill.
3. Check the result against the user's intent and any agreed reference outputs.
4. Show the result and differences. Ask for the user's feedback and clarify it.
5. If the user confirms the result, stop. Otherwise, repeat using the feedback.
