# Feature Contract Template

## Purpose

Use this template to define a feature before setup or implementation work begins.

## Template

### Feature ID And Name

- Feature ID:
- Feature name:

### Goal

- What capability exists when this feature works?

### Actors

- Primary actor:
- Secondary actors:

### Trigger

- What starts this feature or flow?

### Preconditions

- What must already be true?

### Inputs

- What data, command, prompt, or UI action enters the system?

### Outputs

- What visible result or durable result should exist afterward?

### Affected Systems

- Database:
- CLI:
- Daemon or backend:
- Config or YAML:
- Prompts:
- Website UI:
- User documentation:

### Documentation Impact

- Documentation status: required_update | reviewed_no_change | not_applicable
- Documentation surfaces:
- Documentation rationale:

### Runtime And Processing Behavior

- What runtime decisions or background processing occur?

### Supported Behaviors

- Which supported records, commands, interactions, or rendering behaviors are explicitly in scope?

### Known Unsupported Cases

- Which cases are out of scope, deferred, or only planned?

### Failure Handling

- What can fail?
- What should happen then?

### Failure Handling Actually Implemented

- Which recovery or diagnostic behaviors truly exist now?
- Which failure paths remain future work and must not be overclaimed in docs?

### Recovery And Retry

- What must be restart-safe, retry-safe, or idempotent?

### Invariants

- What must never happen?

### Documentation Claim Boundary

- What may `docs/user/`, `docs/operator/`, `docs/reference/`, and `docs/runbooks/` say as supported behavior?
- What must those docs describe as limitation, warning, or future work instead?

### Proof Surface

- Documentation verification:
- Bounded proof:
- Real E2E target:
- Required E2E command:
- E2E readiness status:
- Last stronger proof result:

### Governed File Mapping

- Rigid feature definition file:
- Snapshot baseline file:
- Required governed files that should change:
- Governed files reviewed-no-change:
- Key files for milestone gates:

## Rule

Feature names alone are not sufficient. A feature is not defined until trigger, inputs, outputs, failures, invariants, and proof posture are explicit.

If the repository is beyond pure template use, the feature contract should agree with the rigid feature-definition file rather than leaving governed files implicit in prose.
