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

## Development Operation Logging Rule

All meaningful work must leave a durable development log under `notes/logs/`.

Development logs must record:

- what was attempted
- what changed
- what commands and tests were run
- what passed or failed
- what remains blocked, deferred, or partial

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
