---
name: workplan
description: "Use when the user asks for an investigation, implementation, or fix that will not finish in one session: many steps, several repos, or long runs. Also use when the user asks to plan such a task. Creates `workplans/<topic>/` with objective.md, tasks.md, and report.md, and plans the work before it starts."
---

# Workplan

A workplan carries one long task across sessions in three local documents. The documents hold the intent, the plan, and the findings. A later session enters through `objective.md`, as the coding guidelines direct, and keeps the other two current.

## Location

- `workplans/<topic>/` at the root of the working directory. `<topic>` is lower-case kebab-case, the words the user uses for the task.
- The folder is local and temporary. Keep it out of git without editing tracked files:

  ```bash
  git check-ignore -q workplans || echo 'workplans/' >> "$(git rev-parse --git-dir)/info/exclude"
  ```

## Documents

| File | Purpose | Content | Update when |
|---|---|---|---|
| `objective.md` | Plan, Guide | Goal, scope, guidelines, verification criteria, report contents | The user changes the goal or adds guidance |
| `tasks.md` | Plan, Progress | Subtasks in order, with their plan and status | A task starts, finishes, or changes |
| `report.md` | Report | Findings, analysis, conclusions, verification result | A finding is made or a question closes |

Templates are in `templates/` next to this file. Each template carries its own format rules in its first lines; keep those lines in the created file.

## Workflow

1. Ask the user what is unclear about the request before writing anything: the goal, the reason behind it, the finished state, what is out of scope, known constraints, and where the relevant code and data are. Collect the questions and ask them together.
2. Copy the three templates into `workplans/<topic>/`. Fill `objective.md` from the answers. Keep the baseline guidelines. Propose the verification criteria and the procedure.
3. Show `objective.md` to the user. Ask for corrections and for guidance to add to the Guidelines section. Repeat until the user confirms the goal, the scope, and the verification.
4. Explore the code and data the task touches. Do not plan from assumptions. Report what was found and ask the user about decisions that need domain knowledge: algorithms, tradeoffs, priorities, data to use.
5. Fill `tasks.md`. Group the tasks into phases, mark the parallel ones, and keep the verification task last. Adjust the sections of `report.md` to what `objective.md` requires; leave them empty.
6. Show `tasks.md` to the user. Ask which tasks to drop, split, reorder, or delegate. Repeat until the user agrees to the plan.
7. Start the first task. During the work, follow the guidelines in `objective.md`.

## Rules

- Follow the `write-doc` skill in all three files.
- Do not delete the folder. The user removes it when the task is closed.
- When the work changes behavior, commands, or structure, use the `sync-docs` skill as usual. The workplan does not replace the project documents.
