---
name: workplan
description: "Use when the user asks for an investigation, implementation, or fix that will not finish in one session: many steps, several repos, or long runs. Also use when the user asks to plan such a task. Creates local workplan documents, task worktrees and artifact directories, and plans the work before it starts."
---

# Workplan

A workplan carries one long task across sessions in three local documents: the intent, the plan, and the findings. A later session enters through `objective.md`.

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
| `objective.md` | Goal, workspace paths, guidelines, verification, what the report should answer | The user changes the goal or adds guidance |
| `tasks.md` | Subtasks in order, with their plan and status | A task starts, finishes, or changes |
| `report.md` | Results and history: findings, attempts, analysis, conclusions, verification | Something relevant is learned |

Templates are in `templates/`. Keep their first lines.

## Workflow

1. Ask the user what is unclear: the goal, the reason, the finished state, what is out of scope, constraints, where the code and data are. Ask the questions together.
2. Create `workplans/<topic>/` with `worktrees/` and `artifacts/`, then copy the templates into it. Fill `objective.md`, including the absolute workspace paths. Keep the baseline guidelines. Propose the verification.
3. Show `objective.md`. Ask for corrections and guidance. Repeat until the user confirms it.
4. Explore the code and data the task touches. Report the findings and ask about decisions that need domain knowledge: algorithms, tradeoffs, priorities, data.
5. Fill `tasks.md`.
6. Show `tasks.md`. Ask what to drop, split, reorder, or delegate. Repeat until the user agrees.
7. Create or reuse the required Git worktrees under the topic folder, from the intended base revisions. Record each checkout in `objective.md`, then start the first actionable task there.
