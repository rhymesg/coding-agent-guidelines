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
- Start execution after the user approves the initial objective and plan. The approval covers every phase: work to the end without pausing between phases or waiting for user input, within the approved goal, constraints, and permissions.
- On resuming, read `objective.md`, `plan.md`, and `tasks.md` in order. Check them against actual files, results, and running work, and update them before continuing.

### Execution

- Keep the approved goal and completion criteria unchanged unless the user changes them. Adjust verification methods as needed.
- Repeat: do the next ready task, verify it on the real result, update `tasks.md`, and adjust `plan.md` as needed.
- When blocked, investigate the cause, try meaningful alternatives, and continue independent work.

### Workspace

- Create or reuse Git checkouts from the intended base revisions at `worktrees/<repo>/` within this folder, using `<repo>-<purpose>` for additional checkouts.
- Record absolute workplan, worktree, and artifact paths, source repositories, task branches, and base revisions here. Use the recorded paths when starting or resuming.
- Store temporary results, analysis, and scratch files in `artifacts/`.
- Add other documents when needed and link them from `plan.md` or `tasks.md`.

### Delegation

- Delegate independent tasks to multiple agents and run them in parallel when useful.
- Only the main session edits `objective.md`, `plan.md`, and `tasks.md`. Give each subagent this objective, its task, and its assigned worktree/artifact paths.

### Completion

- End only when the goal's verification criteria are met or evidence shows no meaningful path forward within the approved constraints.
- Record the goal's verification evidence and limitations in `tasks.md`, then set `Status` to `completed`.
- Then delete what can be regenerated: unpacked bags with a `.zstd` beside them, logs whose results `tasks.md` records, and build folders.
