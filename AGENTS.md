# Coding Agent Guidelines

## Interaction with the User

- Keep it under 100 words, in sections and bullets.
- Skip background the user already knows.
- Give everything you show the user as a link they can click to view: a file inside the session's folders, or an artifact. Open the files you edit in the app's side pane, if it has one: one file in the file pane, several in the diff pane.
- Edit only on the user's explicit request or approval. Questions, opinions, and statements alone do not authorize edits.
- In work expected to last over 30 minutes, such as a workplan or a batch of runs or tests, start each message sent while working with:
  - **Goal:** for example `Implement <feature> by the <topic> workplan`.
  - **Progress:** for example `Task 1.3 of 4.4`, or `3/8 runs done: 2 passed, 1 failed; checking the failed case`.
  - **Expected end:** the estimated finish time, when known.

## Working

- A skill's rules and workflow steps take precedence over these defaults while it runs.
- When continuing an active workplan, including after compaction, read its `workplans/<topic>/objective.md`.
- Do not run tests or simulations that require manual UI interaction. Report when such verification is needed.
- Do what you can first. Collect any required user input or actions and ask for them together.
- When the user asks about something independent of the current session's work, suggest handling it in a separate session, and offer to start one.

## When Other Sessions Are Running

- Get a time window before a load-sensitive or long, many-core run.
- Announce when such a run ends, which frees the machine, and when you merge, which may require dependent work to rebase before its heavy tests.
- While waiting for a time window, a merge, or another session's result, keep a background wait running so messages reach you.
- In a worktree, give its containers their own name, for example `COMPOSE_PROJECT_NAME=<repo>-<topic>`, so they do not replace those of another checkout of the same repository.
- Talk to the manager session when one has announced itself; it arranges the work centrally through the [manage-sessions](skills/manage-sessions/SKILL.md) skill. Otherwise, talk to the other sessions directly; when many are running, suggest that the user open a manager session.

## Finishing

- Do not commit unless asked; when asked, use the [commit](skills/commit/SKILL.md) skill for committing changes.
- Do not sign your work, such as "Generated with Claude Code" or a co-author line, in commits, merge requests, comments, or other text you publish.
- After Git work in a repository, return its main working tree to its tracked branch and fast-forward it to the remote.
- When your work is merged, remove its worktrees outside workplan folders and their local and remote branches.
- Keep a workplan folder and its worktrees for 14 days after their last change.

## Answering

Answer in this order. Omit sections with nothing to say.

1. State the result under headings that name the work.
2. Under `Skill improvements`:
   - When the user requests further edits to a skill's output, suggest adding the reusable instruction to the skill.
   - When work performed through a skill produces a potentially reusable script or other artifact, suggest incorporating it into that skill.
3. Under `Left behind`, list what remains, as checked just now: uncommitted files, unpushed commits, unmerged branches and merge requests, or worktrees still in place outside `workplans/`. Omit it when nothing remains.
4. Under `Questions`, ask the user about any suggestions or approvals needed. List more than one question as a numbered list.
