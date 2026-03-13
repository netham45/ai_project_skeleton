# Stage 04: Feature Delivery

## Purpose

Feature delivery is where the repository starts shipping real capability from the defined feature and flow contracts while keeping plans, logs, notes, checklists, and bounded proof aligned.

## Required Outcomes

- each meaningful feature has a governing plan
- each feature has a current checklist
- development logs record actual progress and proving
- affected systems are considered explicitly
- bounded tests exist for active changes
- active implementation tasks keep docs, notes, checklists, and test impact synchronized while coding is in progress

## Required Artifacts

- feature plans under `plan/features/`
- task plans under `plan/tasks/`
- feature checklists under `plan/checklists/`
- feature logs under `notes/logs/features/`

## Common Failure Modes

- implementing first and documenting later
- forgetting to update notes when implementation reveals new constraints
- claiming a feature is done because code exists
- using vague overall statuses that hide missing E2E proof
- keeping the original plan while allowing docs, notes, checklists, or test expectations to go stale during coding
- ending a coding session without a stop-point log that says what changed, what was verified, and what still remains

## Delivery Loop Rule

Feature delivery is not governed only at milestone entry.

Once coding starts, every active implementation task should continue to maintain:

- documentation impact
- notes impact
- checklist impact
- test impact
- honest stop-point logging with commands actually run and remaining gaps

Milestone-gate and delivery-loop validators should treat those surfaces as continuously synchronized implementation assets, not as planning-only artifacts that can be ignored once code exists.

## Exit Condition

This stage is operating correctly when new features can be added repeatedly without contributors needing to invent process rules each time.
