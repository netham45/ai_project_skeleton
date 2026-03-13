# Task Plans

Every meaningful implementation or documentation batch should have a governing task plan here before work starts.

At minimum, each task plan should include:

- goal
- scope
- affected systems
- documentation impact
- notes impact
- checklist impact
- test impact
- required documentation changes or a no-change rationale
- canonical verification commands
- documentation verification commands

Implementation-stage tasks should also keep the delivery loop explicit:

- which note or contract surfaces must stay synchronized with the code change
- which checklist surfaces must be updated as status or proving posture changes
- which tests must be added, rerun, or explicitly deferred
- whether the task is allowed to stop in `implemented`, `partial`, `e2e_pending`, or stronger states
