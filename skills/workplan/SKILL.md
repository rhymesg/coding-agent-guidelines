---
name: workplan
description: "Use when starting or planning work that requires multiple sessions, such as an investigation, implementation, or fix."
---

# Workplan

A workplan carries one long task across sessions in four local documents: the intent, the plan, the progress, and the findings. This skill handles initial setup and approval; `objective.md` is the execution entrypoint.

## Location

- `workplans/<topic>/` at the workspace root, or the repository root for a standalone project. `<topic>` is lower-case kebab-case, the words the user uses for the task.
- Reuse the existing topic folder when resuming. Do not create another `workplans/` inside a task worktree.
- Create both `workplans/<topic>/worktrees/` and `workplans/<topic>/artifacts/` when initializing the workplan.
- Create or reuse each repository checkout at `worktrees/<repo>/` within that topic folder. Use `<repo>-<purpose>` for additional checkouts. Perform repository edits, builds and tests there.
- Keep temporary results, analysis and scratch files in `artifacts/`. Record any tool-required output locations, such as a repository’s `logs/`, and preserve needed outputs before removing a worktree.
- Record absolute paths, source repositories, task branches and base revisions in `objective.md`. Give delegated agents their assigned paths; use the recorded paths on resume.
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

Templates are in `templates/`. Keep their purpose statements and choose sections and detail to fit the task; the content above describes each document's role, not required headings.

## Workflow

For an existing workplan, enter through `objective.md`. If setup is incomplete, complete only the missing steps below. Do not recopy templates or repeat recorded approvals.

1. Ask the user what is unclear: the goal, the reason, the finished state, what is out of scope, constraints, where the code and data are. Ask the questions together.
2. Create `workplans/<topic>/` with `worktrees/` and `artifacts/`, then copy the templates into it. Fill `objective.md` with workspace paths, default guidelines, and user guidance. Propose the verification.
3. Show `objective.md`. Ask for corrections and guidance until the user approves it. Record the approval in `objective.md`.
4. Explore the code and data the task touches. Resolve needed user input before execution, including domain decisions, constraints, and access.
5. Fill `plan.md` with the approach and any relevant phases, dependencies, or decisions. Ask for corrections until the user approves it. Record the approval in `objective.md`.
6. Break the agreed plan into concrete tasks in `tasks.md`. Link tasks to the relevant plan sections and mark dependencies and status.
7. After both initial approvals, create or reuse the required Git worktrees from the intended base revisions and record each checkout in `objective.md`. Follow `objective.md` for execution.
