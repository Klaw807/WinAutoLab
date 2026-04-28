# Experiment Workspace

This directory is a self-contained workspace for one experiment and its sub-experiments.

## Layout

```text
.
├── AGENTS.md
├── README.md
├── TODO_GUIDE.md
├── TODO_TEMPLATE.md
├── configs/
├── docs/
├── logs/
├── results/
├── runner.sh
└── runner_lib/
```

## How To Use It

- Edit `runner.sh` to add the experiment commands for this workspace.
- Put checked-in configuration files under `configs/`.
- Write generated outputs to `results/`.
- Keep execution logs under `logs/`.
- Add helper scripts under `runner_lib/` once the runner grows beyond a single file.

Run the default entrypoint with:

```bash
bash runner.sh
```

## Agent Coordination

- `AGENTS.md` gives experiment-local instructions for human and agent collaboration.
- `TODO_GUIDE.md` and `TODO_TEMPLATE.md` are copied from `agent-workflow/` so the experiment can reuse the same task workflow as the workspace without depending on symlink support.
- Create `TODO.md` from `TODO_TEMPLATE.md` once this experiment needs local task tracking for sub-experiments, migrations, or analysis work.
- Add `docs/plans/active/`, `docs/plans/archive/<year>/`, and `docs/plans/history/<year>/` when the experiment starts using the TODO workflow for larger tasks.

## Reuse Boundary

Keep experiment-specific logic here. If a helper becomes useful across multiple experiments, move it into `toolkit/` and call it from `runner.sh` or later helper scripts.
