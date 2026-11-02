---
name: clean-up-workplans
description: "Frees the workspace of finished and abandoned workplans without losing work, data, or findings. Use when the user asks to clean up, prune, or find stale workplans."
---

# Clean Up Workplans

## Criteria

Remove a folder under `workplans/` only when it meets all of these:

- **Not active:** no file or worktree commit changed in the last 14 days, ignoring folder dates, and no running session, process, or container uses it.
- **Nothing local:** every Git checkout inside it, at any depth, has a clean `git status --porcelain`, and its `HEAD` is on a remote branch or merged into its tracked branch, which may have changed the commit hashes.
- **No unique data:** its recordings and logs exist elsewhere or can be regenerated from data that does.
- **Findings recorded:** the conclusions of its `report.md` are in a tracked document, memory, or a merged change.
- **Not an open plan:** its `objective.md` and `tasks.md` leave nothing to do.

An open plan is stale when it is untouched for 14 days and its work is merged, superseded, or obsolete; list it separately for the user to decide.

## Workflow

1. Check every folder against the criteria.
2. Report in chat, numbering items continuously across both headings, and ask which to remove:
   - **Stale open plans:** folder, what remains open, and why it looks stale.
   - **Save first:** old folders kept only for findings, data, or commits stored nowhere else, with what to save and where.
3. Report **Suggested removal** as a numbered list or table: the folders that meet every criterion plus those the user chose in step 2, each with last change, size, and evidence per criterion. Name each dataset in it whose original is in the main working tree, with the original's path.
4. Wait for the user's confirmation of the folders to remove.
5. For each confirmed folder, delete its symbolic links that point outside it, run `git worktree remove` on each worktree inside it, then delete the folder:
   - Add `--force` only when Git refuses because the worktree contains submodules and `git status --porcelain` is empty, or because of local changes the user chose to discard in step 2.
   - Delete files owned by root, left by containers, from inside a container that mounts the folder.
   - Stop and report any other refusal.
6. Run `git worktree prune` in each repository whose worktrees were removed.
