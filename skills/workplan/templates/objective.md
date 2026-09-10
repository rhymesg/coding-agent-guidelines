# <Topic>

Status: ongoing

Objective and execution entrypoint for this workplan. The plan is `plan.md`, the progress is `tasks.md`, and the findings are `report.md`.

Choose sections and detail to describe the goal, scope, constraints, verification, and what the report should answer. Record absolute workplan, worktree, and artifact paths, source repositories, task branches, base revisions, and any tool-required output paths.

## Guidelines

- Check `Status` first: `ongoing`, `paused`, or `finished`. Unless `ongoing`, report it and wait for the user.
- Start execution after the user approves the initial objective and plan. Record actual approvals here and retain them on resuming. Then work without user intervention within the approved goal, constraints, and permissions; choose approaches and resolve uncertainties from available evidence.
- On resuming, read `objective.md`, `plan.md`, and `tasks.md` in order, then relevant findings in `report.md`. Reconcile them with actual files, results, and running work before continuing.
- Repeat: execute the next actionable task, verify the result, update findings in `report.md` and tasks and status in `tasks.md`, revise `plan.md` when planning decisions change, and continue toward the goal.
- Record relevant attempts, findings, hypotheses, assumptions, and open questions in `report.md`. Distinguish verified findings from unverified ideas.
- Only the main session edits `objective.md`, `plan.md`, `tasks.md`, and `report.md`. Give each subagent this objective, its task, and its assigned worktree/artifact paths; it returns findings in its reply.
- Use the recorded workspace paths when starting or resuming. Perform repository edits, builds, and tests in the assigned worktree under this workplan’s `worktrees/`.
- Store temporary results in `artifacts/`; record tool-required output paths and preserve needed outputs before removing completed worktrees.
- When changes accumulate, use the `commit` skill to commit completed, verified units of work and continue. Follow any user-specific commit instructions.
- When blocked, investigate the cause, try meaningful alternatives, and continue independent work. Do not stop merely because one approach fails or the work is difficult.
- Before a session boundary, leave the next action, blockers, and relevant commands, result paths, or running job identifiers in `tasks.md`. A session boundary does not end the task.
- End only when the goal's verification criteria are met or evidence shows no meaningful path forward within the approved constraints. Set `Status` to `finished`. In `report.md`, record verification evidence, conclusions, and limitations for an achieved goal; for an unmet goal, record attempts, evidence, unmet criteria, and why remaining alternatives offer no meaningful path forward.
- Keep current conclusions easy to find. Condense or separate older details while retaining important failures, evidence, and decision reasons.
- Add other documents when needed and link them from `plan.md`, `tasks.md`, or `report.md`.
- Update these defaults and existing guidance when the user gives additional instructions. Replace superseded guidance and avoid duplicates.
