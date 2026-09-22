---
name: integration-test-guidelines
description: "Designs focused tests across component boundaries. Use when the user requests integration tests for component interactions."
---

# Integration Testing Guidelines

## Design

Inspect the project structure, component interactions, and existing tests. Keep user-provided choices and select effective options for the rest:

- **Scope:** Use the smallest boundary that exposes the relevant failures. Connect real components within it and replace dependencies outside it as needed.
- **Scenarios:** Cover normal operation and plausible interaction failures, including ordering, delays, repetition, and recovery where relevant.
- **Inputs:** Use minimal, representative sequences from synthetic inputs or extracted dataset segments, preserving initialization and accumulated history.
- **Expected results:** Define independently justified outcomes and tolerances. Verify existing outputs before using them as references.

## Implementation

- Put each integration test in `integration/<test_name>/` under the project's test directory, with its test file and test data together.
- Start each test file with a header comment summarizing the selected scenarios, component boundary, inputs, and acceptance criteria.
- Include required data, configuration, and timestamps in the repository. For extracted data, record the source and extraction range.
- Exercise production APIs and processing paths while preserving encapsulation.
- Assert behavior, not implementation details.
- Isolate each test's state and resources; control clocks, randomness, and other nondeterministic inputs. Tests must not depend on execution order.
- Make failures identify the scenario, expected behavior, and actual result.
- Include these tests in the project's normal test target, such as `make test`, without manual preparation.

## References

- [Google Testing Blog: Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) — focused integration tests for component interactions.
- [The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) — test boundaries, isolation, repeatability, and maintainable assertions.
