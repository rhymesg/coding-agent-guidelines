---
name: make-mr-and-merge
description: "Takes changes through review, CI, and merge. Use when the user says make mr and merge."
---

# Make MR and Merge

- Complete the workflow through merge unless the user explicitly limits the scope.

## Workflow

1. Identify the affected repository and read its instructions. Fetch main (or the repository's target branch) and work on a branch off it, never on the target branch itself.
2. Use the [commit](../commit/SKILL.md) skill to commit related uncommitted files or hunks to the branch, preserving unrelated work.
3. Check open MRs into the target branch.
   - When one is active (recently updated, running CI, or awaiting merge), agree on the merge order with the session responsible for it.
   - When one conflicts, let it merge first, then integrate this work onto the updated main and recheck.
4. Run relevant checks, push, and create the MR.
5. Wait for CI on the latest commit. Inspect failures, fix test, lint, and build errors, then commit and push until green.
6. Address blocking review comments and verify fixes before resolving discussions. Address suggestions when you agree; explain disagreements.
7. When the latest commit has passing CI, required approvals, no blocking discussions, and no conflicts, merge using the repository's normal method without bypassing protections.
8. Verify the MR is merged and report its link and merge commit.
