---
name: unit-test-guidelines
description: Use when writing, updating, or reviewing unit tests.
---

# Unit Test Guidelines

Use these guidelines when writing, revising, or reviewing unit tests.

- Identify the function's purpose and when it would fail. Explain your understanding before writing.
- Each test should cover one clear behavior under one scenario.
- Keep tests independent, using fakes or mocks for slow or external dependencies.
- Keep setup minimal and test data readable, and assert only what proves the behavior under test.
- Do not derive expected results using the same logic as the code, and do not assert that a constant equals its own literal.
- Cover various inputs that could plausibly break it — typical, boundary, empty, duplicate, malformed, extreme, repeated.

