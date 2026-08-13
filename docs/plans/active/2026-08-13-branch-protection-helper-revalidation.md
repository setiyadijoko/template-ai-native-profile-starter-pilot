# Branch-protection helper revalidation

## Purpose

Verify that the corrected branch-protection helper binds the aggregate's
emitted `Required controls` check run on this disposable Starter consumer.

## Acceptance criteria

1. `gh pr checks --required` returns exactly six checks.
2. The required checks include `Required controls` and the five invariant
   governance contexts.
3. All six required checks complete successfully without a pending context.
4. GitHub records each required check against the GitHub Actions app.
5. This pull request is closed without merge after evidence collection.
6. Branch protection is restored to the original unprotected state.

## Scope

This evidence-only document does not change application code, profile policy,
workflow behavior, deployment configuration, or production state.
