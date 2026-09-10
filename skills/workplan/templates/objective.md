# <Topic>

Status: ongoing

Objective of the workplan in this folder. The plan is `tasks.md`, the findings are `report.md`.

## Goal

- What the user wants and why.
- What the finished state looks like.

## Workspace

- Workplan directory: <absolute topic folder path>.
- Worktrees directory: <absolute workplan directory>/worktrees/.
- Artifacts directory: <absolute workplan directory>/artifacts/.
- Repositories: <source repository, task branch, base revision and absolute worktree path for each checkout>.
- Tool-required output locations: <paths outside artifacts/, if any>.

## Guidelines

- When the user gives guidance before or during the work, record it as a bullet in this list and follow it. Replace any bullet it contradicts.
- Check `Status` first: `ongoing`, `paused`, or `finished`. Unless `ongoing`, report it and wait for the user. Set it `finished` when the verification passes with a conclusion in `report.md`.
- Read and update `tasks.md` as the current plan. Continue from the first actionable task and keep task status current.
- Read `report.md` for results and history. Record attempts, findings, hypotheses, assumptions, and open questions as they arise. Label verified findings.
- Only the main session edits `objective.md`, `tasks.md` and `report.md`. Give each subagent this objective, its task and its assigned worktree/artifact paths; it returns findings in its reply.
- Use the recorded workspace paths when starting or resuming. Perform repository edits, builds and tests in the assigned worktree under this workplan’s `worktrees/`.
- Store temporary results in `artifacts/`; record tool-required output paths and preserve needed outputs before removing completed worktrees.
- Work autonomously within the goal and guidelines. Freely edit and organize `tasks.md` and `report.md`, preserving results, history, and reasons for plan changes.
- After completing and verifying a unit of work, use the `commit` skill to commit its changes.
- Add other documents when needed and link them from `report.md` or `tasks.md`.
- <User's guidance, one bullet each, appended as it arrives.>

## Verification

- Criteria: what the result must meet.
- Data or tests: what measures the criteria.
- Procedure: the command or steps.

## Report

- What the user wants to learn from `report.md`: questions to answer, decisions to support.
- Include a conclusion when the work is complete.
