# Checklists

Checklists are implementation assets, not optional reminders.

Use this folder for:

- project operational state
- bootstrap readiness
- feature status tracking
- audit and flow coverage

When product features are identified, add one checklist file per meaningful user-requested capability.

Per-feature checklist files should preserve the linkage from:

- original vision
- feature inventory
- governing flows
- documentation surfaces
- bounded proof
- real E2E proof

Naming guidance:

- `PF01_feature_name.md`
- `PF02_next_feature_name.md`

Template-only example checklists are allowed only before real `PFxx` product rows exist.

Once real product features exist:

- every real `PFxx` row should have exactly one real checklist file
- placeholder checklist prose should be retired
- E2E asset and proof-status fields should be recorded explicitly
