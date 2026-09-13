# <Topic>

> **Status:** ongoing
>
> Goal and execution rules. Start here.

Keep Goal, Verification, and Guidelines.

## Goal

- Describe the user's desired outcome, including relevant scope and constraints.

## Verification

- Describe how to verify that the user's goal is achieved: criteria, checks, and evidence.

## Guidelines

- Update these defaults and existing guidance when the user gives new instructions.

### Start and Resume

- Check `Status` first: `ongoing`, `paused`, or `completed`. Unless `ongoing`, report it and wait for the user.
- Start execution after the user approves the initial objective and plan. Then work without user input within the approved goal, constraints, and permissions.
- On resuming, read `objective.md`, `plan.md`, and `tasks.md` in order, then relevant findings in `report.md`. Check them against actual files, results, and running work, and update them before continuing.

### Execution

- Keep the approved goal and completion criteria unchanged unless the user changes them. Adjust verification methods as needed.
- Repeat: do the next ready task, verify the result, update `tasks.md` and `report.md`, and adjust `plan.md` as needed.
- When changes build up, use the `commit` skill to commit completed, verified units of work and continue.
- When blocked, investigate the cause, try meaningful alternatives, and continue independent work.

### Workspace

- Create or reuse Git checkouts from the intended base revisions at `worktrees/<repo>/` within this folder, using `<repo>-<purpose>` for additional checkouts.
- Record absolute workplan, worktree, and artifact paths, source repositories, task branches, and base revisions here. Use the recorded paths when starting or resuming.
- Store temporary results, analysis, and scratch files in `artifacts/`.

### Delegation

- Delegate independent tasks to multiple agents and run them in parallel when useful.
- Only the main session edits `objective.md`, `plan.md`, `tasks.md`, and `report.md`. Give each subagent this objective, its task, and its assigned worktree/artifact paths.

### Report

- Record relevant attempts, findings, hypotheses, assumptions, and open questions in `report.md`. Label verified findings and unverified ideas clearly.
- Keep current conclusions easy to find. Shorten or separate older details while keeping important failures, evidence, and reasons for decisions.
- Add other documents when needed and link them from `plan.md`, `tasks.md`, or `report.md`.

### Completion

- End only when the goal's verification criteria are met or evidence shows no meaningful path forward within the approved constraints.
- Record verification evidence, conclusions, and limitations in `report.md`, then set `Status` to `completed`.
