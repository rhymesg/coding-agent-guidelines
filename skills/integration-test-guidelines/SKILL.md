---
name: integration-test-guidelines
description: Use when the user requests integration tests for component interactions, including state and output changes over time.
---

# Integration Testing Guidelines

Test interactions among a small set of real components in normal CI. Verify how input order, timing, repetition, and accumulated history affect internal state and outputs.

## Design

1. Inspect the project structure, component interactions, and existing tests.
2. Present the following design choices to the user:
   - **Test scenarios:** Which existing behaviors to preserve, including representative normal operation.
   - **Test boundary:** Which real components to connect and which dependencies outside that boundary to replace.
   - **Input data:** Which synthetic inputs or extracted dataset segments represent the scenarios.
   - **Acceptance criteria:** Pass/fail criteria, tolerances, and whether reference outputs have been verified as correct.
3. Obtain the user's approval of the design before implementing the tests.

## Implementation

- Choose tools and implementation methods that fit the project.
- Use the smallest input sequences that reproduce the scenarios. Include any required data in the repository.
- Include the inputs, configuration, and timing needed for initialization and state accumulation. For extracted data, record the source and extraction range.
- Give each test independent state and resources. Tests must not depend on other tests or execution order.
- Changes made for testing must not alter or bypass the actual processing flow or behavior.

## Verification

- Inspect internal state only as needed for verification. Preserve production encapsulation.
- Obtain and verify outputs through the same public functions used by external modules.
- Use explicit assertions for success or failure. Make tests repeatable and failures easy to diagnose.
- Run tests in normal CI without manual preparation. Failed tests must fail the CI job.
- Before updating expected results, confirm the intended behavior change and the new results' basis.
