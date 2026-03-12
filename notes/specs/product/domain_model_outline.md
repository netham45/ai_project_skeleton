# Domain Model Outline

## Purpose

Describe the starter entities, state language, and durable records that the intended product scope depends on before setup begins.

## Starter Questions

- What are the primary entities the system acts on?
- Which records must be durable for audit, recovery, or restart safety?
- Which states or lifecycle phases matter for those entities?
- Which relationships must remain reconstructible later?
- Which fields or records are operator-facing versus internal?

## Minimum Starter Structure

For each major entity, record:

- name
- purpose
- durable or not
- key relationships
- lifecycle states
- audit or recovery significance
- owning system

## Rule

Do not let setup or implementation invent durable records, lifecycle states, or relationship terms that this note has not at least outlined honestly.
