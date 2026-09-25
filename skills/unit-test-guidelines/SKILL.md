---
name: unit-test-guidelines
description: "Designs focused tests of observable behavior. Use when planning, writing, or updating unit tests."
---

# Unit Test Guidelines

- Identify the function's purpose, then name the bug each test would catch. Skip tests where you cannot name one, including tests of framework behavior and trivial getters.
- Cover inputs that could plausibly break the function — typical, boundary, empty, duplicate, malformed, extreme, repeated.
- Cover one behavior under one scenario per test.
- Keep branches and loops out of test bodies; use one parameterized case per condition.
- Keep tests independent, using fakes or mocks for slow or external dependencies.
- Control time, randomness, and external inputs with fixed values or test doubles.
- Keep setup minimal and test data readable.
- Keep test-only methods out of production classes.
- Assert only what proves the behavior under test, and derive expected results without the code's own logic.
- Assert the outcome, not only that the result is non-null or that no exception is thrown.
- Do not assert text, labels, styles, or values that the code states literally; they fail on edits, not on faults. Assert the behavior they depend on instead.
- Before finishing, imagine small bugs in the code and confirm a test would catch each one.
