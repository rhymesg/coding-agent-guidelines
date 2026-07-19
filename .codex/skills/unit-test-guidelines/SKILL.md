---
name: unit-test-guidelines
description: Use when writing, updating, or reviewing unit tests.
---

# Unit Test Guidelines

Use these guidelines when writing, revising, or reviewing unit tests.

- Verify observable behavior or side effects, not implementation details.
- Before writing tests, identify the function's real purpose, invariants, inputs, outputs, and failure modes.
- Write tests that fail for plausible wrong implementations, not tests that merely execute the current code.
- Each test should cover one clear behavior under one scenario.
- Keep tests independent, using fakes or mocks for slow or external dependencies.
- Keep setup minimal and test data readable.
- Assert only what proves the behavior under test.
- Do not copy production logic into tests to compute expected results.
- Do not test constants or literals unless they define observable behavior.
- Cover meaningful normal, boundary, empty, invalid-input, and error cases.
- Use parameterized tests when the same behavior applies to multiple cases.
- Name tests by subject, scenario, and expected result.
- A failing test should make the broken behavior clear.
