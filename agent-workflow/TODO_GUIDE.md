# TODO_GUIDE.md

> Rules for using TODO.md collaboratively between Human and Agent.
- The template of TODO.md is [TODO_TEMPLATE.md](TODO_TEMPLATE.md)

---

# Core Principle

Each task must answer:

1. What exactly to do?
2. Where to do it?
3. How to know it is done?
4. Any dependency or blocker?

If unclear, rewrite task first.

---

# Good Task Standard

Tasks should be:

- Small (1 focused session)
- Observable
- Specific
- Actionable
- Independent when possible
- Linked to a detailed doc in `docs/plans/active/` when the work is too large for `TODO.md`

---

# Status Legend

- [ ] TODO
- [>] DOING
- [x] DONE
- [-] BLOCKED
- [~] CANCELLED

---

# Ownership Rules

Use:

- owner: human
- owner: agent
- owner: shared

Agent should avoid modifying `owner: human` tasks unless asked.

---

# Agent Workflow

1. Read `Current Focus`
2. Pick highest-priority unblocked task
3. If the task needs a detailed plan, create the `TODO.md` entry first, create and link the local plan doc, then start implementation
4. Work on one task only
5. When the task is completed, archive its plan doc in the same change that marks the task `[x]`
6. Create or move the task's history file under `docs/plans/history/<year>/` when a task is closed

## Plan And History Lifecycle

Use `TODO.md` as the source of truth for task status.

For tasks that need a detailed active plan doc:

- create the doc in `docs/plans/active/`
- use filename format `YYYY-MM-DD_<TASKID>_<slug>.md`
- store the canonical link in the task's `details:` field
- when helpful, store the closed-task log link in a separate `history:` field after closure
- keep `where:` focused on implementation targets, not plan storage

Status mapping:

- `[ ]`, `[>]`, `[-]` -> `details:` points to `docs/plans/active/...` when an active plan exists
- `[x]`, `[~]` -> for plan-driven tasks, `details:` points to `docs/plans/archive/<year>/...`
- `[x]`, `[~]` -> for plan-driven tasks, `history:` points to `docs/plans/history/<year>/...`
- `[x]`, `[~]` -> for non-plan tasks, `details:` may point directly to `docs/plans/history/<year>/...`

Active plan doc header should include:

- title
- linked task ID
- optional status note that explicitly defers to `TODO.md`
- created date
- last updated date

Closed-task history files should use the same filename format: `YYYY-MM-DD_<TASKID>_<slug>.md`

History file header should include:

- title
- linked task ID
- status
- created date
- closed date
- last updated date

History file body should include:

- `## Summary`
- `## Outcome`
- `## History Log`
- `## Notes`

Optional sections for larger tasks:

- `## Decisions`
- `## Implementation Notes`
- `## Follow-Ups`
- `## References`

`## History Log` should preserve the detailed dated task/session log that used to accumulate in project-level update logs.

Use short dated bullets such as:

- `2026-04-22` created the task and linked the active plan
- `2026-04-22` made the workflow decision to move closed tasks into `docs/plans/history/<year>/`
- `2026-04-22` completed the task and converted the active plan into the closed-task record

## Closed Task Lifecycle

`TODO.md` is intentionally not the permanent ledger.

Use these roles:

- `TODO.md` -> active control plane for current priorities, backlog, blocked work, and a very small recent-closure window
- `docs/plans/active/` -> in-flight detailed plans for tasks that need them
- `docs/plans/archive/<year>/` -> preserved completed design/plan docs for plan-driven tasks
- `docs/plans/history/<year>/` -> closure record and dated task log for every closed task

When a task closes:

1. mark the task `[x]` or `[~]` in `TODO.md`
2. if it has an active plan doc, move it unchanged to `docs/plans/archive/<year>/`
3. if it has an archived plan doc, create a companion history file in `docs/plans/history/<year>/`
4. if it does not have an active plan doc, create a short history file in `docs/plans/history/<year>/`
5. for plan-driven tasks, update `details:` to point to the archived plan and `history:` to point to the history file
6. for non-plan tasks, `details:` may point to the history file directly
7. keep the task in `# Recently Done` only as a short coordination window
8. prune older closed tasks from `TODO.md` after their durable files exist

Important:

- do not drop detailed task/session logs when pruning `TODO.md`
- preserve them in the task's own `## History Log` section
- the per-task history file replaces the old global update-log behavior for that task
- do not rewrite the archived plan into a closure summary; preserve it as the design record

Pruning rule:

- `# Recently Done` should stay small
- target at most 3 entries
- only the most recent closed tasks that still help active coordination should remain in `TODO.md`
- older closed tasks belong only in `docs/plans/history/<year>/`

Lessons learned / non-negotiable agent behavior:

- if a session creates or materially revises a plan-driven task, add or update the `TODO.md` task entry before doing the work
- create the local plan doc and link it from `details:` before implementation starts
- do not leave a completed task pointing at `docs/plans/active/`
- for plan-driven tasks, move the completed plan to `docs/plans/archive/<year>/` and create the history file in the same session
- for non-plan tasks, create the completed task's history file in the same session that finishes the task
- do not treat `TODO.md` as the durable project journal
- record durable closure/history in `docs/plans/history/<year>/`, not in a growing `# Done` or `# Update Log` section
- preserve detailed dated task logs inside each task's history file instead of discarding them

---

# Human Workflow

## Morning

- Set priorities
- Add tasks
- Clarify vague tasks

## During Day

- Coordinate ownership
- Review progress

## End of Day

- Review done tasks
- Add next tasks
- Clean stale tasks

---

# Conflict Prevention

- Preserve task IDs
- One active task per owner
- Do not rewrite unrelated tasks
- Add new ideas to Backlog first

---

# Golden Rule

`TODO.md` is not notes and not the permanent history.

It is the project control plane.
