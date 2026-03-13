# AGENTS.md

## Purpose

This repository is being built as a spec-driven system.

Work in this repo must stay aligned with the design notes and authoritative note assets in `notes/`.
Implementation is not allowed to drift away from the notes silently.

If coding reveals a limitation, contradiction, missing behavior, needed elaboration, verification gap, runtime mismatch, command inconsistency, checklist mismatch, or lifecycle-stage mismatch, the relevant note, checklist, plan, or lifecycle artifact must be updated in the same change or in an immediately adjacent follow-up change.

This repository does not permit undocumented behavior, undocumented verification steps, undocumented operational assumptions, silent narrowing of behavior to a more convenient implementation path, or completion claims that exceed the actual proving level.

## Lifecycle Governance Rule

Before meaningful work begins, read:

- `notes/lifecycle/00_project_lifecycle_overview.md`
- the current lifecycle stage note under `notes/lifecycle/`
- `plan/checklists/00_project_operational_state.md`

Follow the rules for the lifecycle stage the repository is actually in.

Treat stage-specific requirements as belonging to the lifecycle notes and operational-state checklist, not as ad hoc process rules to invent from memory.

Do not claim statuses or proving levels that the current stage and its completed sub-steps do not justify.

After any `/compact` or equivalent context-compaction event, re-read the full lifecycle-governance state before resuming work.

That re-read must include:

- `notes/lifecycle/00_project_lifecycle_overview.md`
- the current lifecycle stage note under `notes/lifecycle/`
- `plan/checklists/00_project_operational_state.md`
- the currently governing task plan under `plan/tasks/`, if one exists for the active work

Do not rely on pre-compact memory, earlier commentary summaries, or inferred momentum to continue lifecycle-governed work after compaction.

## First Unchecked Item Rule

For lifecycle-governed work, always begin by identifying:

- the active lifecycle stage from `plan/checklists/00_project_operational_state.md`
- the first unchecked, unverified, or still-in-progress item in that active stage

That first incomplete item is the only valid starting point.

Do not select a later item because it seems more efficient, more important, or more convenient.

Do not infer a better ordering from chat context if the governing checklist already establishes the order.

If the first incomplete item is ambiguous, resolve that ambiguity from the repository artifacts before editing anything else.

## Single Checklist Item Execution Rule

When work is being driven by a lifecycle checklist, stage checklist, readiness checklist, or other governing checklist, complete exactly one checklist item per edit batch.

A single edit batch means the smallest coherent set of file changes required to complete one checklist item honestly.

Do not combine multiple checklist items into one pass, even if they appear adjacent, small, or closely related.

Do not update downstream artifacts "while you are there" unless the current checklist item explicitly requires those updates for its own completion.

If one checklist item reveals another missing prerequisite, finish and record the current item honestly, then move to the newly determined next item in a separate edit batch.

## Autonomous Continuation Rule

"One checklist item at a time" does not mean "stop after one checklist item."

Unless blocked by missing information, a hard repository constraint, or an explicit user pause, continue autonomously from the current completed checklist item to the next single incomplete checklist item within the same turn.

Do not end the turn merely to announce the next step.

Do not wait for user confirmation between sequential checklist items unless the user explicitly asked for that stop-and-wait behavior.

## Lifecycle Progression Rule

`AGENTS.md` defines the always-on doctrine for the repository.

As the lifecycle progresses, the repository's standards should become stricter through the lifecycle notes, operational-state checklist, and governing task plans rather than by silently changing contributor expectations in chat history.

Use the lifecycle artifacts this way:

- `AGENTS.md` defines the permanent cross-stage rules, system model, proving doctrine, and update obligations.
- `notes/lifecycle/*.md` define the stage-specific standards, required artifacts, common failure modes, and exit conditions.
- `plan/checklists/00_project_operational_state.md` records which stage and sub-steps are actually active.
- `plan/tasks/*.md` define the concrete work package and canonical verification commands for the current batch.

When the lifecycle advances, contributors should update the stage-governance artifacts that changed and update `AGENTS.md` only when the always-on doctrine changed too.

Examples:

- if a new lifecycle stage is added, update the lifecycle overview, the affected stage notes, and the operational-state checklist; update `AGENTS.md` only if the standing governance model changed
- if a new primary system, permanent proving rule, or global completion rule is adopted, update `AGENTS.md` as part of the same change
- if only a stage-specific expectation changed, keep that detail in the stage notes and checklists instead of bloating `AGENTS.md`

## No Implicit Stage Advancement Rule

Do not describe a lifecycle stage as complete, advanced, ready, or unlocked unless all of the following are true:

- every required checklist item for that stage is actually complete
- the required artifacts for those items actually exist
- required logs and checklist updates for those items have been made
- the required verification commands for the claimed proving layer have actually been run and passed

Do not use phrases such as:

- "this effectively completes the stage"
- "the repo is now at the next stage"
- "the next stage is now allowed"

unless the governing artifacts have been updated honestly and the prior stage is actually complete on its own terms.

Inference is not completion.
Partial progress is not stage advancement.

## No Bundled Lifecycle Advancement Rule

Do not advance multiple lifecycle stages in one pass.

Do not collapse genesis, architecture, product definition, setup, feature delivery, or later stages into a single broad effort such as "reconciliation," "bootstrapping," or "getting the repo into a real state."

Each lifecycle stage must be satisfied in order, and each required checklist item within that stage must be completed discretely.

Even if later-stage work seems obvious, do not begin it until the earlier stage is actually complete and the governing artifacts honestly say so.

## Lifecycle Maturity Ladder

Use this shorthand to understand how repository expectations tighten over time:

- `genesis`: define mission, systems, stack direction, unknowns, and bootstrap governance
- `architecture`: define authority, durability, boundary lines, and stack ownership
- `product definition`: define major flows, feature outlines, contracts, domain model, operator surfaces, and implementation slices
- `setup`: create the scaffold and bounded-proof surface for the defined starter scope
- `feature delivery`: implement features against the defined contracts while keeping plans, logs, checklists, and notes aligned
- `hardening and end-to-end proof`: prove the intended runtime narratives through real boundaries and revisit resilience, performance, and audit expectations
- `post-v1 evolution`: reopen only the lifecycle obligations affected by the new workstream

## Core Implementation Model

Every feature must be considered across the repository's declared primary systems.

No feature is complete until its effect on all applicable systems has been considered explicitly.

The default starter systems for this repository are:

### 1. Database

The database is the durable source of truth for state, lineage, history, and recovery-critical records.

### 2. CLI

The CLI is the operational interface for both human operators and AI sessions.

### 3. Daemon Or Backend

The daemon or backend is the live runtime authority.

### 4. Config Or YAML

Config assets define declarative structure and policy, but they must not silently absorb live runtime authority that belongs in code.

### 5. Prompts

Prompts are first-class implementation assets when AI behavior is part of the product or development workflow.

### 6. Website UI

The website UI is the browser operator surface when the product includes one.

If a starter project truly does not use one of these systems, mark that system explicitly as `not_applicable` in the governing plan, checklist, or review context.

## Stack Declaration Rule

This starter repository is intentionally language, framework, and toolkit agnostic.

Primary stack decisions belong to genesis and architecture work, not to the starter `AGENTS.md`.

Before setup or feature work claims a stable foundation, the repository should declare its chosen stack in the relevant notes, such as:

- `notes/catalogs/inventory/system_inventory.md`
- `notes/specs/architecture/code_vs_config_delineation.md`
- `notes/specs/architecture/authority_and_api_model.md`

## System Coverage Rule

Tests must cover all applicable systems touched by a feature, flow, or contract.

It is not acceptable to test only the most convenient or fastest surface when the described behavior spans multiple systems.

If one of the declared systems is truly not affected, that must be a deliberate conclusion recorded in the governing artifact for the work.

## Task Plan Rule

No meaningful code or process change should happen without a governing task plan under `plan/tasks/`.

Task plans must include:

- the goal
- the scope
- affected systems
- relevant notes
- canonical verification commands
- intended proof layer

## Minimal Edit Scope Rule

For any checklist-driven task, edit only the files required to satisfy the current checklist item.

Do not widen the edit scope to include anticipated future work, convenience refactors, adjacent cleanup, or downstream stage preparation unless the current checklist item explicitly requires it.

If additional needed work is discovered, record it in the proper governing artifact and address it when it becomes the active next item.

## No Reframing Rule

Do not rename, broaden, or reinterpret the current work item into a larger effort category unless the repository artifacts explicitly define that broader category as the active work item.

Examples of forbidden reframing include turning a specific checklist item into:

- "lifecycle reconciliation"
- "setup slice"
- "product-definition completion pass"
- "governance cleanup"
- "feature bootstrap"

The governing checklist item is the unit of execution.
Use the repository's terms, not improvised umbrella descriptions.

## Development Operation Logging Rule

All meaningful work must leave a durable development log under `notes/logs/`.

Development logs must record:

- what was attempted
- what changed
- what commands and tests were run
- what passed or failed
- what remains blocked, deferred, or partial

## Checklist And Commentary Separation Rule

Commentary is not progress.

Status updates must describe the exact governing checklist item currently being executed and the exact artifact being changed for that item.

Do not use commentary to imply broader completion than the edit batch actually accomplished.

Do not substitute summaries, plans, or explanations for required checklist completion, file updates, or verification.

## User Correction Lock Rule

If the user corrects how the repository instructions must be followed, that correction becomes binding for the rest of the turn unless it directly conflicts with a higher-priority repository rule.

Do not reinterpret the correction into a looser version.

Do not comply briefly and then return to a broader self-directed approach.

When corrected, immediately align execution behavior to the user's stated control rule and keep that rule active until the user changes it.

## System Invariants Rule

Every meaningful subsystem must have explicit invariants documented in `notes/` or another approved design artifact.

Tests must defend invariants, not only features.

If implementation depends on an invariant that has not been written down yet, the work is incomplete.

## Checklist Enforcement Rule

Every meaningful feature must have a checklist entry that tracks implementation and verification status across all affected systems.

Checklists must explicitly record:

- affected systems
- implementation status
- bounded test status
- E2E status
- notes status
- known limitations
- overall status

If a system is not affected, mark it explicitly rather than omitting it.

## Checklist Maintenance Rule

Checklists are part of the implementation surface.

They must be updated whenever:

- code changes affect a tracked feature
- test status changes
- E2E status changes
- canonical commands change
- a new limitation is discovered
- the overall feature status changes

## Authoritative Document Rule

Authoritative document families are part of the implementation surface.

If a document family is authoritative, it must have automated consistency tests that enforce:

- required sections
- allowed status vocabularies
- required mappings
- required references
- family-specific invariants

Whenever an authoritative document changes, run the relevant document consistency tests afterward.

## Notes Maintenance Rule

The notes and authoritative note assets in `notes/` are part of the implementation surface.

They must be updated whenever work reveals:

- a limitation in the current design
- an ambiguity that must be resolved
- a contradiction between notes
- a new invariant
- a newly discovered failure mode
- a new recovery or concurrency constraint
- a testing expectation change
- a verification-command change
- a checklist or lifecycle mismatch

## Relevant Flow Rule

Relevant user and operator flows must be tracked through:

- narrative flow notes or walkthroughs
- a structured flow inventory when the repo adopts one

If implementation changes a relevant flow materially, update both surfaces together.

## Canonical Verification Command Rule

Build, test, validation, migration, flow, audit, and performance commands must be explicitly documented.

Do not rediscover proving commands ad hoc during implementation.

If a note or checklist claims something is verified, it must cite the documented canonical command that actually passed.

## Per-Item Verification Rule

When a checklist item has a relevant verification command, run only the verification needed to support completion of that item.

Do not defer item-level verification until several later items have also been changed.

Do not claim an item complete if its required verification for the claimed proving layer has not actually been run.

If no verification is yet applicable for that item, state that explicitly in the governing artifact or commentary rather than implying proof exists.

## Test Progression Rule

Testing must progress in stages.

### Stage 1: Bounded Proof

Bounded, simulated, mocked, or fixture-assisted tests are required during implementation and review.

### Stage 2: Real End-To-End Proof

Every feature intended to exist in real runtime usage must progress to full real E2E proof through the relevant system boundaries.

Bounded tests do not count as final completion proof for real runtime behavior.

There is no feature so small, simple, or low-risk that it is exempt from real E2E coverage.

No feature is complete without full real E2E tests for its intended scope.

If full E2E proof does not yet exist, the feature may be labeled:

- `implemented`
- `in_progress`
- `partial`

It may not be labeled:

- `complete`
- `flow_complete`
- `release_ready`

unless the real E2E layer has been completed for the intended scope.

## E2E Coverage Rule

Every feature must be exercisable in real code.

Every meaningful feature must map to at least one explicit real E2E test target.

There is no feature too small to require a real E2E test.

Grouped or batched E2E narratives are acceptable, but traceability is still required.

One E2E file per feature is not required.

If the strongest proof still bypasses the core runtime boundary being claimed, the feature is not E2E-covered.

A feature is not E2E-covered if its strongest proof still relies on:

- fake backends or fake session layers
- in-process runtime bridges as the only proof
- direct durable-state mutation to skip runtime work
- synthetic prompt, summary, result, or equivalent workflow injection
- staged placeholders instead of real source-control, session, provider, external-service, or environment behavior where the feature depends on those boundaries

If a feature depends on another feature, both may share one E2E narrative, but both must be tracked explicitly as covered by that E2E suite.

### Live-Run Equivalence Rule

Any test claimed as E2E must test every claimed workflow component as if it were being used in a real live run.

This rule is absolute.

For repository claim purposes, a test is not E2E unless:

- every claimed workflow step happens through the same runtime boundary used in real operation
- every claimed component is exercised through its real role in that workflow
- the test waits for the real system to perform the work being claimed
- the asserted outcome is the result of that real runtime path rather than a shortcut or injected state

There is no acceptable "mostly real" interpretation.

If even one claimed workflow step is skipped, forced, injected, mocked, manually advanced, or satisfied through a lower-layer shortcut, the test must not be treated as E2E coverage for that workflow.

### Forbidden In E2E Rule

The following are forbidden in any test that is claimed as E2E coverage for a workflow:

- fake backends or fake session layers
- direct durable-state mutation to force the workflow into a later state
- in-process runtime bridges as the strongest proof
- synthetic prompt, summary, result, session, or equivalent workflow injection
- direct API or RPC completion shortcuts such as a test-only "complete step" endpoint
- test-side `task start`, `task complete`, or `task fail` actions when those actions are supposed to come from live runtime behavior
- test-side `summary register` or equivalent result-publication shortcuts when the summary or result is supposed to be produced by the live runtime
- test-side `workflow advance` or equivalent transition forcing when the runtime is supposed to advance the workflow itself
- manual descendant or child creation in a test that claims the AI or runtime created those descendants itself
- hidden helper behavior that performs the workflow step off-screen and then exposes only the end result
- using a lower-layer proof to stand in for a higher-layer E2E claim

If any of those are present, the workflow is not E2E-covered. The required remediation is to remove the simulation or shortcut and make the test perform the real workflow through the live runtime path. Do not delete, skip, or permanently downgrade the E2E requirement because the test is difficult.

### E2E Naming And Claim Rule

No test, note, checklist, command catalog, plan, review, or assistant response may describe a workflow as E2E-covered, real-E2E-passing, `flow_complete`, or equivalent unless the exact live-run-equivalent workflow has actually been rerun and passed.

The fact that a harness uses real infrastructure does not make the test E2E if any claimed workflow step is still synthetic.

If a file under `tests/e2e/` is only a bring-up target, partially simulated narrative, or bounded or operator-assisted proof, that status must be stated explicitly and it must be excluded from canonical passing E2E command sets.

Simulation and E2E are opposites in this repository. A simulated workflow may still be useful at a lower layer, but it is never a substitute for the required real E2E proof and it does not reduce the obligation to implement that proof.

## Completion Standard

No feature or change is complete without tests.

No feature is small enough to be excused from full real E2E proof.

A feature is complete only when all of the following are true:

- relevant notes are current
- implementation matches the notes
- invariants are explicit
- affected systems are explicitly accounted for
- the feature checklist is current
- required development logs are current
- required bounded tests exist
- required real E2E tests exist for the intended scope
- required document consistency tests exist for changed authoritative document families
- canonical verification commands are documented
- those commands were actually run for the claimed layer
- known limitations are documented explicitly

No feature is complete without full real E2E proof for its intended scope.

## Turn-End Constraint

If the user has told you to proceed, continue executing the governed sequence until one of the following is true:

- the requested governed scope is actually complete
- you are blocked by missing information that cannot be resolved from repo context
- the repository rules require a user decision
- the user explicitly interrupts, pauses, or redirects the work

Do not end the turn merely because:

- one checklist item was completed
- you identified the next step
- you want confirmation on an obvious next item
- you have a partial progress summary to share

## Completion State Vocabulary

Use these terms deliberately:

- `implemented`: assets or code exist and bounded proof may exist, but full real E2E proof is not yet complete
- `verified`: the documented verification command for the claimed layer actually passed
- `partial`: some intended behavior exists, but limitations or missing proving layers remain
- `flow_complete`: the intended user or operator flow passed end to end for the declared scope
- `release_ready`: all required bounded tests, real E2E tests, readiness docs, and checks are complete for the declared release scope

Do not describe work as complete if it is only implemented.

## Testing Standard

Tests must be all-encompassing for meaningful behavior.

All tests are expected to be runnable in parallel.

Test isolation is part of correctness, not optional hardening.

A test that passes only when run serially and fails because of parallel execution, shared mutable state, fixture contention, resource collision, or cross-test interference is defective and must be treated as an issue to fix.

External capability gating is a separate concern.

It is acceptable to gate tests on genuinely unavailable requirements such as source-control tooling, provider credentials, external services, browsers, terminals, or similar explicit environment capabilities.

It is not acceptable to normalize serial-only execution because the test or fixture design is not parallel-safe.

That includes:

- normal behavior
- invalid inputs
- boundary cases
- failure paths
- pause paths
- retry paths
- recovery paths
- persistence behavior
- database behavior where applicable
- CLI behavior where applicable
- backend or daemon behavior where applicable
- config compilation behavior where applicable
- prompt-contract behavior where applicable
- auditability and inspectability expectations
- concurrency behavior where relevant
- idempotency where relevant
- migration or compatibility behavior where relevant
- authentication and authorization behavior where relevant

Bounded tests are required during initial implementation and code review.

Full real E2E tests are required before final completion.

Authoritative document-family consistency tests are required wherever document families are part of the implementation surface.

If a feature mutates durable state, the mutation rules must be tested through the real persistence layer where applicable, not only through mocked or in-memory paths.

If a feature depends on ordering, concurrency, retries, recovery behavior, CLI contracts, backend contracts, config compilation, prompt delivery, or other real runtime boundaries, those semantics must be tested explicitly at the proper system boundary.

If a feature is difficult to test, that is a sign the design or implementation should be improved until it becomes testable.

## Test Layer Contracts

Tests must be written intentionally at the correct layer.

Parallel-safety applies at every layer.

Unit, integration, performance, resilience, document-consistency, and end-to-end tests should all be able to coexist under parallel execution when their required environment capabilities are present.

Layer choice is not an excuse for shared mutable fixtures or cross-test interference.

### Unit And Bounded Tests

Use these tests for:

- branch logic
- validation rules
- state-machine legality
- transformation logic
- invariant enforcement
- failure classification
- prompt or rendering contracts
- small persistence rules with narrow scope
- fast review-time feedback during implementation

These tests are required during initial implementation but are not final completion proof for real runtime behavior.

They must still be parallel-safe and must not rely on shared mutable process, filesystem, database, schema, or environment state.

### Integration Tests

Use integration tests for:

- boundaries between major subsystems
- migrations
- runtime coordination across modules
- config compilation and runtime policy application
- audit, history, and provenance persistence
- auth, session, or external-service boundaries
- flow slices that cross major subsystem boundaries

### End-To-End Tests

Use end-to-end tests for:

- real user or operator flows
- real process or service boundaries
- real persistence and recovery behavior
- real source-control, session, provider, or external-service coordination where applicable
- full setup-to-outcome flows with no fake skipping of critical boundaries

Critical end-to-end flows must not simulate away the core behavior being claimed.

Simulation and E2E are antonyms in this repository: if a workflow step is simulated, injected, forced, or skipped, the test is not E2E.

For avoidance of doubt:

- an E2E test must execute the workflow as a live run would execute it
- every component named by the workflow must be exercised in that live-run-equivalent path
- if the runtime is supposed to create, advance, summarize, merge, recover, finalize, or otherwise progress something, the E2E must wait for the runtime to do exactly that
- if an operator surface is the thing being tested, the E2E may use that real operator surface, but it may not use hidden lower-layer shortcuts to fake the rest of the workflow

An E2E test that mixes real boundaries with synthetic workflow progression is defective and must not be counted as E2E proof.

E2E is the final required proving layer for any feature that is supposed to exist in real runtime behavior.

Do not remove, skip, or waive E2E coverage because implementation is difficult. The correct response to a defective simulated E2E is to make the test run the real workflow.

Real-runtime resource needs such as ports, workspaces, databases, browsers, terminals, tokens, source-control repositories, or external-service sandboxes must be isolated so eligible E2E tests can run concurrently.

### Document Consistency Tests

Use document consistency tests for:

- required document structure
- status vocabulary enforcement
- feature, checklist, and E2E mapping integrity
- command reference consistency
- required section and field presence
- document-family-specific invariants

### Performance Tests

Use performance tests for:

- repeated inspection or query paths
- compilation cost
- runtime scheduling or coordination overhead
- durable-store query efficiency
- startup and recovery overhead
- any path explicitly designated performance-sensitive

### Resilience Tests

Use resilience tests for:

- interruption
- restart
- retry after partial completion
- duplicate request handling
- stale-session or stale-runtime recovery
- durable audit and recovery correctness after failure

## Risk-Based Testing Rule

Every feature, flow, and checklist should explicitly consider:

- data loss risk
- silent corruption risk
- concurrency risk
- recovery complexity
- operator confusion risk
- auditability risk

## Required Execution Pattern For Lifecycle-Governed Work

When performing lifecycle-governed work, follow this exact pattern repeatedly:

1. Read the active stage from `plan/checklists/00_project_operational_state.md`.
2. Identify the first incomplete item in the active governing checklist.
3. Name that item explicitly in commentary.
4. Edit only the artifact(s) required for that one item.
5. Update only the minimal tracking surfaces required for that one item.
6. Run only the verification required for that one item, if applicable.
7. Report that item's result honestly.
8. Immediately continue to the next first incomplete item unless blocked.

Forbidden substitutions:

- jumping ahead to a later item
- batching multiple checklist items into one edit pass
- announcing a future step instead of doing it
- inferring stage completion from momentum
- treating broad summaries as checklist completion
- performance risk
- cross-system contract risk

Higher-risk behavior deserves deeper testing.

## Adversarial Flow Rule

Planned flows should include, where applicable:

- happy path
- invalid input path
- retry path
- pause or interruption path
- recovery path
- conflicting action path
- partial-completion path
- operator diagnosis path
- blocked or impossible state path

## Performance Rule

Performance is part of correctness where the repository depends on repeated inspection, compilation, orchestration, or large state surfaces.

Where performance matters, notes or checklists should define explicit budgets or thresholds.

## Observability And Auditability Rule

A behavior is not fully implemented unless operators can inspect and explain it.

Implementation and tests should account for:

- what durable records are written
- how an operator inspects current state
- how failure causes are inspected
- how lineage and provenance are reconstructed
- how recovery readiness is inspected

## Implementation Expectations

For every meaningful feature, consider explicitly:

1. database changes
2. CLI changes
3. daemon or backend changes
4. website UI changes
5. config or YAML changes
6. prompt changes
7. note updates
8. invariants
9. affected systems
10. canonical verification commands
11. bounded tests
12. E2E tests
13. checklist updates
14. development log updates
15. document consistency tests
16. performance impact
17. observability and auditability impact
18. recovery and concurrency impact

If one of these is not affected, that should be a deliberate conclusion rather than an assumption.

## Stack Decision Maintenance Rule

Do not let primary stack choices remain implicit once the repository has actually chosen them.

When genesis or architecture work selects primary languages, frameworks, persistence layers, test tools, UI stacks, or prompt tooling, record those decisions in the relevant notes, verification commands, and checklists before acting as if they are settled.
