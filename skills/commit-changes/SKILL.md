---
name: commit-changes
description: "Use when the user asks Codex to commit changes in this project, including requests like 'commit', '커밋해줘', '나머지도 커밋', or when Codex needs to prepare git commits from the current working tree. Formats first, groups changes by logical unit, and creates unsigned one-line commit messages."
---

# Commit Changes

Use this workflow to create clean project commits from the current working tree.

## Workflow

1. Inspect the working tree before staging.

   ```bash
   git status --short
   git diff -- <paths>
   ```

2. Handle untracked files before committing: add intentional files, delete junk, or update `.gitignore` for recurring generated artifacts.

3. Run formatting before committing.

   Try the host command first:

   ```bash
   make format
   ```

   If it cannot run on the host, run the project Docker formatter:

   ```bash
   docker exec mnav_navigation_desktop bash -c "cd /mnav_workspace && make format"
   ```

4. Re-check `git status --short` and diffs after formatting. Treat formatter-only edits as their own logical unit when they are unrelated to feature changes.

5. Split commits by logical change. Stage only files belonging to one unit at a time. Do not stage unrelated dirty files or broad untracked directories unless the user explicitly includes them.

6. For each logical unit, request approval with `git add` and `git commit` in one command line. Keep the command scoped to the files in that unit and use an unsigned, one-line commit message.

   ```bash
   git add <paths> && git commit --no-gpg-sign -m "Short imperative message"
   ```

## Commit Message Rules

- Use exactly one `-m` argument.
- Do not add a body, trailers, signatures, or co-author lines.
- Prefer short imperative English messages, for example `Add ground altitude store`.
- Keep formatting-only commits explicit, for example `Format map tile selector files`.

## Safety

- Never revert or discard user changes to make a commit cleaner.
- If a file contains mixed unrelated changes, stage only the requested hunks when practical; otherwise ask before committing it.
- After each commit, show the commit hash and what remains uncommitted.
