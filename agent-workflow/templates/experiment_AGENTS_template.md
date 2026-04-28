# Agent Workflow Overlay

When using an agent for help inside this experiment, add prefix "Use AGENTS.md as the guide of your following work" to your conversation.

This experiment root is the control boundary for experiment-specific work, sub-experiments, run tracking, and local notes.

Before modifying this experiment, read:
- [README.md](README.md) - experiment purpose, layout, and runner usage
- [TODO.md](TODO.md) - local live task control plane when present
- [TODO_GUIDE.md](TODO_GUIDE.md) - canonical TODO workflow reused from `agent-workflow`
- [docs/plans/](docs/plans/) - local detailed plans and task history when present

Use `TODO.md` for local experiment task state when the experiment grows large enough to need one. Create it from `TODO_TEMPLATE.md` rather than inventing a new structure.

## Ownership Rules

- Keep experiment-specific scripts, configs, and notes in this experiment root.
- Keep generated outputs under `results/` and execution logs under `logs/`.
- Move reusable helpers, libraries, and cross-experiment utilities back to `toolkit/`.
- Keep long implementation detail in `docs/plans/` when the experiment adopts a local TODO workflow.

## Engineering Rules

- Prefer minimal focused changes
- Reuse toolkit patterns before adding experiment-local utilities
- Update docs when experiment behavior changes
- Run relevant checks before completion
- Add tests when adding code or reusable helpers
