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

### Runtime And Processing Behavior

- What runtime decisions or background processing occur?

### Failure Handling

- What can fail?
- What should happen then?

### Recovery And Retry

- What must be restart-safe, retry-safe, or idempotent?

### Invariants

- What must never happen?

### Proof Surface

- Bounded proof:
- Real E2E target:

## Rule

Feature names alone are not sufficient. A feature is not defined until trigger, inputs, outputs, failures, invariants, and proof posture are explicit.
