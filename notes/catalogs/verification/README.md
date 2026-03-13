# Feature Snapshot Baselines

This folder stores per-feature snapshot baselines for the rigid feature-definition model.

Each baseline should:

- belong to one `PFxx` feature
- hash only the files declared in that feature's definition file
- support `created`, `modified`, `deleted`, and `unchanged` reporting
- remain read-only during normal test runs
- only be refreshed through an explicit snapshot-update command

Defining a real E2E command in the feature definition satisfies the requirement that the feature has an E2E target.

It does not mean the E2E proof passed.
