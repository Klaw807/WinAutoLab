# Personal Workspace Template

Compare-first workspace template for evaluating external repos, running experiments, and later growing into a project-owned codebase when needed.

## Structure

```text
workspace/
├── agent-workflow/   # reusable workflow baseline and scaffolding
├── toolkit/          # reusable personal tools
├── repos/            # external repos, forks, submodules
├── experiments/      # evaluation workspaces and outputs
├── docs/
└── README.md
```

## Folder Roles

- `agent-workflow/`: reusable agent workflow rules, TODO templates, and scaffolding guidance
- `toolkit/`: reusable cross-project infrastructure kept as a git submodule
- `repos/`: upstream or external code; keep each repo's history and ownership separate
- `experiments/`: comparison and benchmark work that should not live inside a source repo
- `docs/`: project-level plans, durable notes, and other shared documentation

## Two Phases

### Compare Phase

Use this workspace as-is when you are comparing frameworks or testing multiple repos.

- put external code in `repos/`
- run evaluation work under `experiments/`
- keep shared collaboration workflow in `agent-workflow/`
- move reusable helpers into `toolkit/`

### Build Phase

When the workspace becomes project-owned implementation, add these root folders:

- `src/`
- `tests/`
- `scripts/`
- `configs/`

Use them for your own code. Keep upstream repos in `repos/`. Update the AGENTS.md for phase changed.

## Promotion Checklist

When you decide to build your own implementation:

1. Add root `src/`, `tests/`, `scripts/`, and `configs/`.
2. Keep upstream code and submodules in `repos/`.
3. Keep `TODO.md` and `docs/plans/` local to the project root even when reusing `agent-workflow/`.
4. Update local docs and instructions to say the workspace is now in implementation mode.

## Experiments

Create a new experiment from the workspace root:

```bash
./experiments/start
```

That creates:

```text
experiments/YYYY-MM-DD_name/
```

with local `AGENTS.md`, `README.md`, `runner.sh`, `runner_lib/`, `configs/`, `results/`, and `logs/`.

Use each experiment root for self-contained evaluation work:

- `runner.sh` as the entrypoint
- `configs/` for checked-in experiment inputs
- `results/` for generated outputs
- `logs/` for execution logs

## Setup

Sync toolkit and stage the workspace pointer update:

```bash
bash setup.sh
```

## Git Strategy

- workspace = git repo
- agent-workflow = reusable workflow package intended to be shared across projects
- toolkit = git submodule
- repos/* = independent git repos

## Shared TODO Files

This workspace reuses the canonical shared files directly from `agent-workflow/`:

- `TODO_GUIDE.md` from `agent-workflow/TODO_GUIDE.md`
- `TODO_TEMPLATE.md` from `agent-workflow/TODO_TEMPLATE.md`

Keep `TODO.md` local to the workspace or experiment that owns the work, and link larger tasks to `docs/plans/`. Do not rely on root-level symlinks for shared workflow Markdown files.
