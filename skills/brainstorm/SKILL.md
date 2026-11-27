---
name: brainstorm
description: "Clarifies what the user wants and how to build and verify it before any work starts. Use when the user wants to implement something, make a plan, or start a workplan, including 'do it with workplan'."
---

# Brainstorm

Do not edit code or create workplan documents while brainstorming.

## Clarify intent

Clarify the user's intent before developing the proposal. When the goal, scope, constraints, or success criteria are unclear, ask focused questions until you reach a shared understanding.

Find facts yourself. Never ask the user for information you can discover from the environment. When clarification requires investigation, dispatch a subagent with a fresh context window. While it investigates, ask any questions that do not depend on its findings.

Once the intent is clear, suggest methods and verification using the proposal format below. Resolve choices through applicable instructions and requirements; present recommendations and alternatives for choices left open.

## Proposal

Once the intent is clear, reply with one proposal each turn, up to about 300 words including tables:

- `Intent`: what you understand the user wants: goal, scope, constraints, and success criteria, as applicable.
- Following sections as appropriate, such as approach and open decisions. State each choice the guidelines, rules, or requirements settle in the approach, with the rule named.
- `Suggestions`, until the user picks an option or persuades you, and again when the intent changes:
  - Viable alternatives for each choice the guidelines, rules, and requirements leave open, such as architecture or method, weighed on simplicity, maintainability, readability, expandability, and best practice. Present them as a table, labelling each option `(recommended)`, `(yours)`, or `(existing)` where applicable:

    | Option | Trade-offs |
    |---|---|
    | A. Short name of the option (label) | Its strengths and costs on the criteria above |
  - Candidate verification methods, weighed on practical criteria, no blind spots, repeatability, regression coverage, and automation. Once chosen, present them as a table:

    | Check | Evidence | Pass when |
    |---|---|---|
    | What is verified | Log, tool output, or measurement that shows it | The threshold or condition that counts as success |
  - Where applicable, the documents to update, such as architecture notes and READMEs:

    | Document | Content |
    |---|---|
    | Path of the file | What it gains or how it changes |
  - Where applicable, the Makefile targets the user needs to follow and run the work:

    | Target | Script | What it does |
    |---|---|---|
    | `make <target>` | Script the target runs | Its effect |
  - Your recommendation with reasons.

## Workflow

1. Clarify the intent, then show the proposal and wait for the user's answers.
2. Refine it with each answer until consequential questions are resolved or explicitly deferred.
3. Before the user approves a plan, have a fresh subagent read the code each change touches, with every caller, and report changes that do not match that code, target states no change produces, phases that need a later phase's work, and inputs only the user can give. Fix the plan and ask for those inputs together.
4. Suggest the next step:
   - Work that fits one session: the agent's plan mode in the current session.
   - Work spanning several session windows: an explicit `/create-workplan` call.
