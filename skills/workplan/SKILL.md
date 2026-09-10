---
name: workplan
description: "Use when starting or planning complex work that requires multiple sessions."
---

# Workplan

A workplan tracks one long task across sessions in four local documents: the goal, the plan, the progress, and the findings. This skill handles initial setup and approval; execution starts with `objective.md`.

## Location

- `workplans/<topic>/` at the workspace root, or the repository root for a standalone project. `<topic>` is lower-case kebab-case, the words the user uses for the task.
- Create both `workplans/<topic>/worktrees/` and `workplans/<topic>/artifacts/` when setting up the workplan.
- The folder is local and temporary. Keep it out of git:

  ```bash
  git check-ignore -q workplans || echo 'workplans/' >> "$(git rev-parse --git-path info/exclude)"
  ```

## Documents

| File | Content | Update when |
|---|---|---|
| `objective.md` | Goal, scope, constraints, workspace paths, guidelines, verification, what the report should answer | The user changes the goal or adds guidance |
| `plan.md` | Approach, phases, dependencies, key decisions and reasons | A planning decision changes |
| `tasks.md` | Concrete tasks in order, links to the plan, status | A task starts, finishes, or changes |
| `report.md` | Results and history: findings, attempts, analysis, conclusions, verification | Something relevant is learned |

Templates are in `templates/`. Keep their purpose statements and the `Goal`, `Verification`, and `Guidelines` sections in `objective.md`; choose other sections and detail to fit the task.

## Workflow

For an existing workplan, start with `objective.md`. For a new or incomplete workplan, follow the steps below.

1. Ask the user what is unclear: the goal, the reason, the finished state, what is out of scope, constraints, where the code and data are.
2. Create `workplans/<topic>/` with `worktrees/` and `artifacts/`, then copy the templates into it. Fill `objective.md` with the goal, workspace paths, default guidelines, and user guidance. Plan how to verify that the user's desired outcome is achieved, and record the criteria, checks, and evidence to collect in `Verification`.
3. Show `objective.md` and propose the verification plan to the user. Ask for corrections and guidance until the user approves it.
4. Explore the code and data the task touches. Get needed user input before execution, including domain decisions, constraints, and access.
5. Fill `plan.md` with the approach and any relevant phases, dependencies, or decisions. Ask for corrections until the user approves it.
6. Break the agreed plan into concrete tasks in `tasks.md`. Link tasks to the relevant plan sections and mark dependencies and status.
7. Start execution following `objective.md`.
