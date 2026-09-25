# xUnit Test Smells

Summary of the code and behavior smells in Gerard Meszaros, [xUnit Test Patterns: Test Smells](http://xunitpatterns.com/Test%20Smells.html). Project-level smells are left out.

- SUT: the code under test. Fixture: what a test sets up before it calls the SUT.
- Fresh fixture: built by each test for itself. Shared fixture: reused across tests or runs.

## Code Smells

### [Obscure Test](http://xunitpatterns.com/Obscure%20Test.html)

The reader cannot tell at a glance what behavior the test verifies.

| Cause | Sign | Fix |
|---|---|---|
| Eager Test | One test verifies many behaviors | Split it into one test per condition |
| Mystery Guest | Setup or expected data live outside the test, such as in a file or shared fixture | Build the data in the test |
| General Fixture | Setup builds far more than the test uses | Build a minimal fresh fixture per test |
| Irrelevant Information | Many values that do not affect the outcome | Default them in a creation helper |
| Hard-Coded Test Data | Literals whose relation to the expected result is unclear | Name the values that matter; relate expected values to inputs without the SUT's logic |
| Indirect Testing | The test reaches the SUT through another object, such as the UI | Test the SUT directly, or hide the path behind helpers |

### [Conditional Test Logic](http://xunitpatterns.com/Conditional%20Test%20Logic.html)

The test contains branches or loops, so which code runs is unclear.

| Cause | Sign | Fix |
|---|---|---|
| Flexible Test | The expected result depends on the environment, such as the current time | Replace the dependency with a test double; write one test per case |
| Conditional Verification Logic | `if` statements or loops around assertions | Use a guard assertion, an expected object, or a custom assertion |
| Production Logic in Test | The expected value repeats the SUT's calculation | Use a table of precalculated inputs and expected values |
| Complex Teardown | Cleanup code with branches | Use a fresh fixture or automated teardown |
| Multiple Test Conditions | A loop applies one check to many inputs and stops at the first failure | Use a parameterized test with one case per condition |

### [Test Code Duplication](http://xunitpatterns.com/Test%20Code%20Duplication.html)

| Cause | Sign | Fix |
|---|---|---|
| Cut-and-Paste Code Reuse | The same statements are copied across tests | Extract a creation method or a custom assertion |
| Reinventing the Wheel | New code repeats an existing test helper | Use the existing helper |

### [Test Logic in Production](http://xunitpatterns.com/Test%20Logic%20in%20Production.html)

| Cause | Sign | Fix |
|---|---|---|
| Test Hook | Production code branches on whether it runs under test | Move the behavior into a dependency that tests replace |
| For Tests Only | Methods or public fields that only tests use | Move them to a test-specific subclass or test code |
| Test Dependency in Production | The production build needs test code | Move shared code into a production module |
| Equality Pollution | `equals` added or changed only for tests | Use a custom assertion or comparator in the tests |

### [Hard-to-Test Code](http://xunitpatterns.com/Hard%20to%20Test%20Code.html)

| Cause | Sign | Fix |
|---|---|---|
| Highly Coupled Code | A class cannot be tested without several others | Break the coupling with test doubles |
| Asynchronous Code | The test must start a thread or process and wait for it | Separate the logic from the asynchronous mechanism and test it synchronously |
| Untestable Test Code | The test body is complex enough to doubt its correctness | Move logic into tested helpers |

## Behavior Smells

### [Assertion Roulette](http://xunitpatterns.com/Assertion%20Roulette.html)

The failure output does not show which assertion failed.

| Cause | Sign | Fix |
|---|---|---|
| Eager Test | One test calls several methods, mixing setup and assertions | Split it into single-condition tests |
| Missing Assertion Message | Several assertions of one kind without messages | Give each a distinct message |

### [Erratic Test](http://xunitpatterns.com/Erratic%20Test.html)

The test passes on some runs and fails on others.

| Cause | Sign | Fix |
|---|---|---|
| Interacting Tests | Fails when other tests are added, removed, reordered, or fail | Use a fresh fixture per test; reset static state |
| Resource Leakage | Tests slow down or start failing over time | Release resources in teardown, also on failure |
| Resource Optimism | Passes in one environment and fails in another | Create the resource in setup |
| Unrepeatable Test | The first run behaves differently from later runs | Keep no state that outlives the run |
| Test Run War | Fails when several people run the tests at once | Give each runner its own sandbox |
| Nondeterministic Test | Results vary between runs | Replace random inputs with fixed boundary values |

### [Fragile Test](http://xunitpatterns.com/Fragile%20Test.html)

The test fails after a change that does not affect the behavior it verifies.

| Cause | Sign | Fix |
|---|---|---|
| Interface Sensitivity | Breaks when an unrelated part of the SUT's interface changes | Call the SUT through test helpers |
| Behavior Sensitivity | Breaks when behavior used for setup or verification changes | Put setup behind creation methods and checks behind custom assertions |
| Data Sensitivity | Breaks when shared test data changes | Use a fresh fixture, or assert the change between before and after |
| Context Sensitivity | Breaks when the time, the date, or a dependency changes | Control the inputs with stubs and a virtual clock |
| Overspecified Software | Mocks prescribe how the code works instead of what it achieves | Verify outcomes through the public interface |
| Sensitive Equality | Objects are compared as strings | Compare the fields that matter |
| Fragile Fixture | Changing a shared fixture for one test breaks others | Give each test its own fixture |

### [Manual Intervention](http://xunitpatterns.com/Manual%20Intervention.html)

| Cause | Sign | Fix |
|---|---|---|
| Manual Fixture Setup | A person prepares the environment before the run | Automate the setup |
| Manual Result Verification | The test prints results and passes unless it throws | Add assertions |
| Manual Event Injection | A person must act during the run | Pass simulated events to the SUT |

### [Slow Tests](http://xunitpatterns.com/Slow%20Tests.html)

| Cause | Sign | Fix |
|---|---|---|
| Slow Component Usage | Tests use a database or another slow component | Replace it with a fake |
| General Fixture | Each test builds a large fixture | Build less per test |
| Asynchronous Test | Explicit sleeps in the test | Test the logic synchronously |
