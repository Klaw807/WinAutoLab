# Agent Workflow

Reusable workflow baseline for human-and-agent collaboration across projects.

## Purpose

`agent-workflow/` owns the shared process layer:

- agent initialization template
- TODO workflow rules
- TODO template
- reusable scaffold templates for agent-ready experiment workspaces

Keep live project state outside this directory:

- project `AGENTS.md` overlays
- project `TODO.md`
- project `docs/plans/`

## Consumption Model

Projects should keep a thin local `AGENTS.md` at the repo root, point it directly at `agent-workflow/TODO_GUIDE.md` and `agent-workflow/TODO_TEMPLATE.md`, and add only project-specific ownership or engineering rules there.

To support Windows cleanly, workflow Markdown files should be copied from this directory during scaffolding instead of being shared through committed symlinks.

## Layout

```text
agent-workflow/
├── AGENTS_TEMPLATE.md
├── README.md
├── TODO_GUIDE.md
├── TODO_TEMPLATE.md
└── templates/
    ├── experiment_AGENTS_template.md
    └── experiment_README_template.md
```
