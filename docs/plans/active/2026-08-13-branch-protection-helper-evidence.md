# Branch-protection helper evidence

## Purpose

Exercise the merged branch-protection helper on this disposable Starter
consumer and verify that all six required contexts resolve on a pull request.

## Acceptance criteria

1. The five invariant governance contexts complete successfully.
2. `Profile policy / Required controls` completes successfully.
3. No required context remains pending after the workflow runs settle.
4. This pull request is closed without merge after evidence collection.
5. Branch protection is restored to this repository's original unprotected
   state.

## Scope

This evidence-only document does not change application code, profile policy,
workflow behavior, deployment configuration, or production state.
