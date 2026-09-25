# Additional Test Anti-Patterns

Anti-patterns common in agent-written tests that neither the [xUnit test smells](xunit-test-smells.md) nor the [unit-test-guidelines](../../unit-test-guidelines/SKILL.md) name. Summarized from [superpowers writing-good-tests](https://github.com/obra/superpowers/blob/main/skills/test-driven-development/writing-good-tests.md) and [managedcode test-anti-patterns](https://skills.managed-code.com/skills/test-anti-patterns/).

| Anti-pattern | Sign | Fix |
|---|---|---|
| Tautological test | The expected value comes from the code under test or its helpers, or a value is compared with itself | Use a literal or a hand-checked value |
| Coverage touching | Calls code without any assertion | Assert the outcome, or delete it |
| Source-text test | Searches a script, configuration, or document for a line | Run it and assert its output, side effects, or exit code |
| Mock assertion | Asserts that a mock exists; fails only when the mock is removed | Assert the real component's behavior, or remove the mock |
| Mock at the wrong level | Mocks a method whose side effect the test depends on | Mock the slow or external layer below it |
| Partial mock data | A mock response lacks fields that real data has | Mirror the complete real structure |
| Loose double | A double accepts any argument, count, or order where these are the contract; one fixture serves both success and error | Assert the arguments; give each branch its own fixture |
| Swallowed failure | `try`/`catch` around assertions, assertions only in `catch`, a missing `await` on an async assertion, commented-out assertions, always-true conditions | Let failures propagate; restore the assertion |
| Mock-heavy test | Mock setup outgrows the test logic | Use real components, or move it to an integration test |
