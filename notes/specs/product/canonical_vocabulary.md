# Canonical Vocabulary

## Purpose

Freeze the starter repository's domain language before setup and implementation spread inconsistent terms across notes, code, prompts, and UI.

## Starter Terms To Define

- actor: the person or system initiating a flow
- operator: the human using the CLI or website UI to inspect or control the system
- user: the person whose work or request the system ultimately serves
- flow: a meaningful user or operator narrative with a bounded goal and proof target
- feature: a capability slice that can be planned, implemented, traced, and proved
- contract: the documented trigger, inputs, outputs, invariants, and proof expectations for a behavior
- durable record: state that must survive restart and support audit or recovery
- bounded proof: fast simulated or document-level evidence used during implementation
- real E2E proof: live-run-equivalent evidence through the real runtime boundaries for the claimed scope

## Rule

If a new note, checklist, prompt, or UI surface needs a new domain term, add it here instead of letting the vocabulary drift implicitly.
