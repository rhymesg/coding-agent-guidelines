# Runtime optimization

## Nominal run

Cost of one unit of operation, for example one second at the nominal sensor rates.

| Part | Calls per unit | Before | Share before | After | Share after |
|---|---|---|---|---|---|
| {function or stage} | {count, with the rate it follows from} | {time} | {%} | {time} | {%} |
| Total | | {time} | 100 % | {time} | 100 % |

Overall: {before → after, ratio}.

## Changes

Use the table below as a guide, adapting it to the project. Add sections as needed.

| Before commit | Change | After commit | Metric: before → after | Improvement |
|---|---|---|---|---|
| {code hash} | {bottleneck and optimization} | {code hash or provisional} | {metric, units, values, and variability} | {absolute or relative change} |
