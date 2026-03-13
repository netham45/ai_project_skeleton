# Implementation Slicing Guide

## Purpose

Define how the starter features should be delivered in slices so setup and early feature work do not have to invent sequencing ad hoc.

## For Each Starter Feature

Record:

- feature ID
- first implementation slice
- why that slice is first
- prerequisite features or notes
- affected systems
- documentation surfaces affected
- bounded proof target
- documentation verification target
- eventual real E2E target
- explicit non-goals for the first slice

## Rule

The first slice should be small enough to prove honestly but large enough to exercise the real cross-system contract that makes the feature meaningful.

## Vision Coverage Rule

Implementation slicing must begin from decomposed product features, not directly from freeform concept prose.

Before choosing the first slice for a product feature, confirm that the feature already has:

- a stable feature ID
- a source-vision reference
- one or more governing flows
- affected systems
- documentation surfaces
- bounded proof target
- eventual real E2E target

If any of those are missing, the feature is not ready for slicing.

## Starter Guidance

- Prefer a first slice that exposes one real user or operator narrative clearly.
- Do not hide required systems by slicing only the easiest layer.
- If a feature depends on another feature's boundary or durable-state rule, record that dependency explicitly.
