# Agent Workflow Overlay

When using an agent for help, add prefix "Use AGENTS.md as the guide of your following work" to your conversation.

This root file is the primary instruction file for this workspace. Follow this agent workflow every time you work here.

Before modifying the workspace, read:
- [README.md](README.md) - workspace purpose and structure
- [docs/plans/](docs/plans/) - local plans for large tasks and migrations
- [TODO.md](TODO.md) - live project control plane
- [agent-workflow/TODO_GUIDE.md](agent-workflow/TODO_GUIDE.md) - canonical TODO workflow, ownership, and plan/history lifecycle rules
- [agent-workflow/TODO_TEMPLATE.md](agent-workflow/TODO_TEMPLATE.md) - canonical TODO structure template when creating local TODOs
- [toolkit/AGENTS.md](toolkit/AGENTS.md) - toolkit-specific guidance when changing toolkit

Use `TODO.md` for current workspace task state, and follow `agent-workflow/TODO_GUIDE.md` for how to structure tasks, manage ownership, and handle plan/archive/history updates.

## Ownership Rules

- Keep reusable utilities in `toolkit/`
- Keep reusable workflow rules and scaffolding in `agent-workflow/`
- Keep external repos in `repos/`
- Keep experiment logic in `experiments/`
- Keep outputs in `experiments/runs/`
- Keep long implementation detail in `docs/plans/`

## Engineering Rules

- Prefer minimal focused changes
- Follow the shared agent workflow every time before applying workspace-local rules
- Reuse toolkit patterns before adding workspace-local utilities
- Update docs when behavior changes
- Run relevant checks before completion
- Add tests when adding code
