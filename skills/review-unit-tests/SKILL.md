---
name: review-unit-tests
description: "Finds unit tests that give false confidence or cost upkeep without catching bugs, and fixes them when asked. Use when the user asks to review or fix unit tests, or to find test anti-patterns."
---

# Review Unit Tests

## Modes

- User-requested fix: apply fixes.
- User-requested review: report findings without editing. Wait for editing instructions unless already provided.

## Workflow

1. Check each test against the rules of the [unit-test-guidelines](../unit-test-guidelines/SKILL.md) skill, the [xUnit test smells](references/xunit-test-smells.md), and the [additional anti-patterns](references/additional-anti-patterns.md).
2. Fix the wrong tests or report findings according to the mode. If a fixed test fails, report the failure as a possible bug.

## Report

- Each finding: the test, the anti-pattern, the fix applied or proposed, and any proposed fix to production code.
