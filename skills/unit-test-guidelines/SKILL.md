---
name: unit-test-guidelines
description: "Designs focused tests of observable behavior. Use when planning, writing, updating, or reviewing unit tests."
---

# Unit Test Guidelines

- Identify the function's purpose and plausible failure modes before writing tests.
- Each test should cover one clear behavior under one scenario.
- Keep tests independent, using fakes or mocks for slow or external dependencies.
- Keep setup minimal and test data readable, and assert only what proves the behavior under test.
- Do not derive expected results using the same logic as the code.
- Do not assert text, labels, styles, or values that the code states literally; they fail on edits, not on faults. Assert the behavior they depend on instead.
- Cover various inputs that could plausibly break it — typical, boundary, empty, duplicate, malformed, extreme, repeated.
