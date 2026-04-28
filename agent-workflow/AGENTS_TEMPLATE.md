# Agent Workflow Template

This file is a reusable template/baseline for initializing a project's root `AGENTS.md`.

It is not the primary runtime instruction file for a host project. The host project's root `AGENTS.md` should be the file agents follow on every task, and that root file should point directly to the shared workflow documents in this directory when needed.

## Template Intent

Use this template to shape a project-local `AGENTS.md` that:

- tells agents to always follow the shared agent workflow
- points agents at `agent-workflow/TODO_GUIDE.md`
- points agents at `agent-workflow/TODO_TEMPLATE.md`
- layers project-specific ownership, repo layout, and engineering rules on top

## Shared Workflow Rules

- Use `TODO.md` as the live control plane for current work.
- Keep detailed active plans under `docs/plans/active/` when a task needs a larger design.
- Move completed plans into `docs/plans/archive/<year>/`.
- Record durable task closure/history in `docs/plans/history/<year>/`.
- Keep project-specific implementation details in the host project, not in this shared workflow package.

## Reuse Boundary

- Put reusable process rules and templates here.
- Put reusable code and libraries in the project's toolkit or utility package.
- Put live project state and project-specific decisions in the host repository.
