# Operator Surface Map

## Purpose

Map the starter inspection and action surfaces for operators before setup creates commands, routes, or pages.

## Surface Areas

### CLI

Record:

- inspection commands the operator will need
- write or mutation commands the operator will need
- confirmations, blocked reasons, and diagnostics that must be visible

### Website UI

Record:

- key routes or screens
- deep-linkable views
- bounded actions the browser may expose
- daemon-owned legality or blocked-state information that must remain authoritative

### Prompted AI Surfaces

Record:

- prompts that act as operator or runtime interfaces
- which command or runtime surface each prompt depends on

## Rule

The browser and CLI may expose actions, but they must not silently become the authority for runtime legality, progression, or durable state.
