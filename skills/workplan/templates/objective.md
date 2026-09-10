# <Topic>

> **Status:** ongoing
>
> Goal and execution rules. Start here.
>
> [Plan](plan.md) · [Tasks](tasks.md) · [Report](report.md)

Keep Goal and Verification below; choose other sections and detail to fit the task.

## Goal

- Describe the user's desired outcome, including relevant scope and constraints.

## Verification

- Describe how to verify that the user's goal is achieved: criteria, checks, and evidence.

## Guidelines

### Start and Resume

- Check `Status` first: `ongoing`, `paused`, or `finished`. Unless `ongoing`, report it and wait for the user.
- Start execution after the user approves the initial objective and plan. Record actual approvals here and keep them on resuming. Then work without user input within the approved goal, constraints, and permissions; choose approaches and resolve open questions from available evidence.
- On resuming, read `objective.md`, `plan.md`, and `tasks.md` in order, then relevant findings in `report.md`. Check them against actual files, results, and running work, and update them before continuing.

### Execution

- Repeat: do the next task ready to start, verify the result, update findings in `report.md` and tasks and status in `tasks.md`, update `plan.md` when planning decisions change, and continue toward the goal.
- When changes build up, use the `commit` skill to commit completed, verified units of work and continue. Follow the user's commit instructions.
- When blocked, investigate the cause, try meaningful alternatives, and continue independent work. Do not stop just because one approach fails or the work is difficult.

### Workspace

- Reuse this topic folder on resuming. Do not create another `workplans/` inside a task worktree.
- Create or reuse Git checkouts from the intended base revisions at `worktrees/<repo>/` within this folder, using `<repo>-<purpose>` for additional checkouts. Perform repository edits, builds, and tests in the assigned worktree.
- Record absolute workplan, worktree, and artifact paths, source repositories, task branches, and base revisions here. Use the recorded paths when starting or resuming.
- Store temporary results, analysis, and scratch files in `artifacts/`. Record any output paths required by tools here and keep needed outputs before removing a worktree.

### Delegation

- Delegate independent tasks to multiple agents and run them in parallel when useful.
- Only the main session edits `objective.md`, `plan.md`, `tasks.md`, and `report.md`. Give each subagent this objective, its task, and its assigned worktree/artifact paths; it returns findings in its reply.

### Records and Guidance

- Record relevant attempts, findings, hypotheses, assumptions, and open questions in `report.md`. Label verified findings and unverified ideas clearly.
- Keep current conclusions easy to find. Shorten or separate older details while keeping important failures, evidence, and reasons for decisions.
- Add other documents when needed and link them from `plan.md`, `tasks.md`, or `report.md`.
- Update these defaults and existing guidance when the user gives new instructions. Replace any guidance the new instructions change and avoid duplicates.

### Handoff and Completion

- Before a session ends, leave the next action, blockers, and relevant commands, result paths, or running job IDs in `tasks.md`. The task continues across sessions.
- End only when the goal's verification criteria are met or evidence shows no meaningful path forward within the approved constraints. Set `Status` to `finished`. In `report.md`, record verification evidence, conclusions, and limitations for an achieved goal; for an unmet goal, record attempts, evidence, unmet criteria, and why remaining alternatives offer no meaningful path forward.
