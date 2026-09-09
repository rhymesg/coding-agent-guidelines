---
name: workplan
description: "Use when the user asks for an investigation, implementation, or fix that will not finish in one session: many steps, several repos, or long runs. Also use when the user asks to plan such a task. Creates `workplans/<topic>/` with objective.md, tasks.md, and report.md, and plans the work before it starts."
---

# Workplan

A workplan carries one long task across sessions in three local documents: the intent, the plan, and the findings. A later session enters through `objective.md`.

## Location

- `workplans/<topic>/` at the root of the working directory. `<topic>` is lower-case kebab-case, the words the user uses for the task.
- The folder is local and temporary. Keep it out of git:

  ```bash
  git check-ignore -q workplans || echo 'workplans/' >> "$(git rev-parse --git-dir)/info/exclude"
  ```

## Documents

| File | Content | Update when |
|---|---|---|
| `objective.md` | Goal, guidelines, verification, what the report should answer | The user changes the goal or adds guidance |
| `tasks.md` | Subtasks in order, with their plan and status | A task starts, finishes, or changes |
| `report.md` | Results and history: findings, attempts, analysis, conclusions, verification | Something relevant is learned |

Templates are in `templates/`. Keep their first lines.

## Workflow

1. Ask the user what is unclear: the goal, the reason, the finished state, what is out of scope, constraints, where the code and data are. Ask the questions together.
2. Copy the templates into `workplans/<topic>/`. Fill `objective.md`. Keep the baseline guidelines. Propose the verification.
3. Show `objective.md`. Ask for corrections and guidance. Repeat until the user confirms it.
4. Explore the code and data the task touches. Report the findings and ask about decisions that need domain knowledge: algorithms, tradeoffs, priorities, data.
5. Fill `tasks.md`.
6. Show `tasks.md`. Ask what to drop, split, reorder, or delegate. Repeat until the user agrees.
7. Start the first actionable task and follow the guidelines in `objective.md`.
