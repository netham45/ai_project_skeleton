# Processing System Contracts

## Purpose

Describe the processing and coordination systems that the starter product needs before setup hardens an implementation path.

## Contract Areas

### Work Admission

- How work enters the system
- who may admit it
- which checks happen before acceptance

### Background Processing

- jobs, queues, schedulers, or polling loops that may exist
- which system owns execution authority
- what observability is required

### Retry And Idempotency

- which operations may retry
- which side effects must be idempotent
- which retries are forbidden or require human intervention

### Concurrency And Ownership

- what can happen in parallel
- what requires serialization
- which system is authoritative when conflicts happen

### Failure And Recovery

- which failures pause work
- which failures are terminal
- how interrupted work becomes inspectable and resumable
- which recovery behavior must be reflected in user or operator runbooks

## Rule

Do not let processing behavior hide inside setup code or daemon assumptions without first naming the contract here.
