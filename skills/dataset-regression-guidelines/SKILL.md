---
name: dataset-regression-guidelines
description: Use when the user requests regression tests using small input segments extracted from real datasets.
---

# Dataset-Based Regression Testing Guidelines

Detect regressions during feature changes or dataset additions. Preserve representative segments of existing datasets as small tests without running the full datasets each time.

- Verify how internal state and outputs change over time and across repeated inputs.
- Account for the effects of input order, intervals, and accumulated history on later state and outputs.

## Design

1. Inspect the project structure and existing dataset tests.
2. Present the following design choices to the user:
   - **Test scenarios:** Which existing behaviors to preserve, including representative normal operation.
   - **Test boundary:** Which objects or components to exercise and which dependencies to replace.
   - **Input data:** Which dataset segments to extract and how they represent the scenarios.
   - **Expected-result basis:** Which results serve as the reference and which differences count as regressions. When using existing outputs, state whether they have been verified as correct behavior.
3. Obtain the user's approval of the design before implementing the tests.

## Implementation Guidelines

- Extract the smallest segments of real datasets that reproduce the scenarios and include them in the repository. Run the tests in normal CI without manual data preparation.
- Include the inputs, configuration, and timestamps needed for initialization and state accumulation. Record the data source and extraction range.
- Choose tools and implementation methods that fit the project. Make tests repeatable and failures easy to diagnose.
- Give each test independent state and resources. Tests must not depend on other tests or execution order.
- Inspect internal state only as needed for verification. Preserve production encapsulation.
- Obtain and verify outputs through the same public functions used by external modules.
- Changes made for testing must not alter or bypass the actual processing flow or behavior.
- When updating expected results for an intentional behavior change, confirm the reason for the change and the basis for the new reference results.
