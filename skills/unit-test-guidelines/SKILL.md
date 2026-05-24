---
name: unit-test-guidelines
description: Use when writing, updating, or reviewing unit tests.
---

# Unit Test Guidelines

Use these guidelines when writing, revising, or reviewing unit tests.

- A test should verify what the code guarantees as an output or side effect, not how the code is written internally.
- Each test should cover one clear behavior under one specific scenario.
- Keep tests independent. Use mocks or fakes for external dependencies when needed to avoid slow, unreliable, order-dependent, or environment-dependent tests.
- Keep test setup minimal and explicit.
- Assert only what proves the behavior under test. Avoid unnecessary assertions or verifications.
- Do not test configuration, constants, magic numbers, or literal strings by copying values from the implementation, unless they define externally observable behavior.
- Do not reproduce the production logic inside the test to compute the expected result. Expected results should come from requirements, simple examples, or known domain behavior.
- Use parameterized tests when the same behavior should be checked for multiple input cases.
- Include meaningful edge cases: empty input, boundary values, invalid input, error paths, and representative normal cases.
- Prefer readable test data over overly generic builders or abstractions.
- Name tests by subject, scenario, and expected result.
  - Example: `Purchase_WhenStockIsZero_ReturnsOutOfStockResult`
- A failing test should clearly indicate which behavior is broken, not just that an internal detail changed.
