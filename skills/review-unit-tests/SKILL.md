---
name: review-unit-tests
description: "Finds and fixes unit tests that give false confidence or cost upkeep without catching bugs. Use when the user asks to review or fix unit tests, or to find test anti-patterns."
---

# Review Unit Tests

## Workflow

1. Check each test against the rules of the [unit-test-guidelines](../unit-test-guidelines/SKILL.md) skill, the [xUnit test smells](references/xunit-test-smells.md), and the [additional anti-patterns](references/additional-anti-patterns.md).
2. Fix the wrong tests. If a fixed test fails, report the failure as a possible bug.

## Report

- Each finding: the test, the anti-pattern, the fix applied, and any proposed fix to production code.
