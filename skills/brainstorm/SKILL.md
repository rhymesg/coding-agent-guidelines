---
name: brainstorm
description: "Clarifies what the user wants and how to build and verify it before any work starts. Use when the user wants to make a plan, discuss how to implement something, or mentions a workplan, including 'do it with workplan'."
---

# Brainstorm

Do not edit code or create workplan documents while brainstorming.

## Proposal

Reply with one proposal each turn, up to about 300 words including tables:

- `Intent`: what you understand the user wants: goal, scope, constraints, and success criteria, as applicable.
- Following sections as appropriate, such as approach and open decisions.
- `Suggestions`, until the user picks an option or persuades you, and again when the intent changes:
  - Viable alternatives for anything with a choice, such as architecture or method, weighed on simplicity, maintainability, readability, expandability, and best practice. Present them as a table, labelling each option `(recommended)`, `(yours)`, or `(existing)` where applicable:

    | Option | Trade-offs |
    |---|---|
    | A. Short name of the option (label) | Its strengths and costs on the criteria above |
  - Candidate verification methods, weighed on practical criteria, no blind spots, repeatability, regression coverage, and automation. Once chosen, present them as a table:

    | Check | Evidence | Pass when |
    |---|---|---|
    | What is verified | Log, tool output, or measurement that shows it | The threshold or condition that counts as success |
  - Where applicable, the documents to add or update, such as architecture notes and READMEs, following the [document-writing-guidelines](../document-writing-guidelines/SKILL.md) skill:

    | Document | Content |
    |---|---|
    | Path of the file | What it gains or how it changes |
  - Where applicable, the Makefile targets the user needs to follow and run the work, following the [makefile-guidelines](../makefile-guidelines/SKILL.md) skill:

    | Target | Script | What it does |
    |---|---|---|
    | `make <target>` | Script the target runs | Its effect |
  - Your recommendation with reasons.

## Workflow

1. Show the proposal and wait for the user's answers.
2. Refine it with each answer until consequential questions are resolved or explicitly deferred.
3. Once the intent is clear, use the [get-second-opinion](../get-second-opinion/SKILL.md) skill on the proposal.
4. Suggest which plan to write next. The next step is always a plan, never implementation:
   - Work that fits one session: a plan file in the current session.
   - Work spanning several session windows: an explicit `/create-workplan` call.
