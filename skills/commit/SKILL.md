---
name: commit
description: "Use when the user asks Coding Agent to commit changes, or when Coding Agent needs to prepare git commits from the current working tree."
---

# Commit

Use this workflow to create clean project commits from the current working tree.

Only start committing when the user explicitly asks for it. If it looks like a good point to commit, suggest it and wait for them to ask.

## Workflow

1. Inspect the working tree before staging.

   ```bash
   git status --short
   git diff -- <paths>
   ```

2. Handle untracked files before committing: add intentional files, delete junk, or update `.gitignore` for recurring generated artifacts.

3. Run formatting and linting before committing if the project supports them. Use documented or obvious project commands.

4. Re-check `git status --short` and diffs after formatting. Treat formatter-only edits as their own logical unit when they are unrelated to feature changes.

5. Split commits by logical change. Stage only files belonging to one unit at a time. Do not stage unrelated dirty files or broad untracked directories unless the user explicitly includes them.

6. Check the index for files you did not stage, immediately before committing. The index belongs to the repository, not to the session, so a commit takes whatever anyone else has staged there.

   ```bash
   git status --short
   ```

   Staged entries outside the unit are someone else's work. Unstage them, then commit.

   ```bash
   git restore --staged <paths>
   ```

7. For each logical unit, stage and commit with `git add` and `git commit` in one command line. Keep the command scoped to the files in that unit and use an unsigned, one-line commit message.

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
- Never `git add -A`, `git add .` or `git commit -a`. Name the paths. Another session may be editing the same checkout, and a working tree that was clean at the start of the session may not be clean now.
- Do not commit secrets, credentials, tokens, private keys, `.env` files, or other security-sensitive local configuration. Add these files to `.gitignore` when they are project-local artifacts that should remain untracked.
- After each commit, show the commit hash and what remains uncommitted.
