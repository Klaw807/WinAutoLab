# Experiments Workspace

Use `experiments/` for experiment-specific orchestration that does not belong in a source repo and is not reusable enough for `toolkit/`.

## Layout

```text
experiments/
├── README.md
├── runner_template.sh
├── start
└── <YYYY-MM-DD_name>/
    ├── AGENTS.md
    ├── README.md
    ├── TODO_GUIDE.md
    ├── TODO_TEMPLATE.md
    ├── configs/
    ├── logs/
    ├── runner_lib/
    ├── runner.sh
    └── results/
```

Run `./experiments/start` from the workspace root to create a new experiment scaffold.

The script prompts for a short experiment name and creates a directory named:

```text
YYYY-MM-DD_name
```

where `YYYY-MM-DD` is today's date and `name` comes from your prompt after normalization to lowercase underscore-separated text.

## Folder Roles

- `runner.sh` is copied from `experiments/runner_template.sh` and includes the default toolkit/logging/Conda setup.
- `AGENTS.md` is copied from `agent-workflow/templates/experiment_AGENTS_template.md` and defines experiment-local agent workflow guidance.
- `README.md` is copied from `agent-workflow/templates/experiment_README_template.md` and explains how to use the experiment root.
- `TODO_GUIDE.md` is copied from `agent-workflow/TODO_GUIDE.md` so experiment tasks can follow the shared workflow without depending on symlink support.
- `TODO_TEMPLATE.md` is copied from `agent-workflow/TODO_TEMPLATE.md` so experiments can add a local `TODO.md` later without inventing a new format.
- `runner.sh` can call the shared toolkit helper `exp_stage_results "${RESULTS_DIR}" "${output_dir}" "<sub_experiment_name>"` to copy artifacts into dated result folders.
- `runner_lib/` is available for later helper shell functions once `runner.sh` grows.
- `configs/` stores checked-in configuration inputs for that experiment.
- `results/` stores generated artifacts only, including logs, metrics, plots, and copied run configs.
- `logs/` stores execution logs written by the generated runner and any other shell entrypoints.

Do not commit source logic under `results/`.

## Managing Multiple Experiments

Different experiments may need different scripts, flags, launchers, or environment assumptions. Keeping each experiment in its own root avoids collisions and makes it easier to archive or compare whole experiment setups.

Recommended pattern:

- `experiments/<experiment_name>/AGENTS.md` for experiment-local agent instructions
- `experiments/<experiment_name>/README.md` for experiment-local usage notes
- `experiments/<experiment_name>/TODO_GUIDE.md` and `TODO_TEMPLATE.md` for shared TODO workflow reuse
- `experiments/<experiment_name>/runner.sh` as the default entrypoint
- `experiments/<experiment_name>/runner_lib/` for later split workflow helpers when needed
- `experiments/<experiment_name>/configs/` for config files consumed by that experiment
- `experiments/<experiment_name>/results/` for generated outputs from that experiment
- `experiments/<experiment_name>/logs/` for generated shell logs

Create `TODO.md` from `TODO_TEMPLATE.md` only when the experiment needs local task tracking for sub-experiments or larger follow-up work.

If a helper becomes useful across multiple experiments, move it into `toolkit/` and import or call it from the runner scripts.

## Naming Experiments And Results

Experiment directories should be named:

```text
YYYY-MM-DD_name
```

Examples:

- `2026-04-22_throughput_baseline`
- `2026-04-22_latency_a100`

Inside `results/`, prefer short labels that describe the actual run:

```text
experiments/<experiment_name>/results/<run_label>/
```

Example:

- `experiments/2026-04-22_throughput_baseline/results/batch32/`

When using `exp_stage_results`, the helper creates:

```text
experiments/<experiment_name>/results/YYYY-MM-DD_self_<sub_experiment_name>/
```

If you omit the sub-experiment name, it falls back to:

```text
experiments/<experiment_name>/results/YYYY-MM-DD_self/
```

and prints a reminder so you can add a clearer label on the next run.

## Example Mapping

One experiment might look like this:

```text
experiments/
├── runner_template.sh
├── start
└── 2026-04-22_throughput_baseline/
    ├── AGENTS.md
    ├── README.md
    ├── TODO_GUIDE.md
    ├── TODO_TEMPLATE.md
    ├── configs/
    │   └── base.yaml
    ├── logs/
    ├── runner_lib/
    ├── results/
    │   └── batch32/
    └── runner.sh
```

Example command:

```bash
bash experiments/2026-04-22_throughput_baseline/runner.sh
```
 
## Bootstrap Script Behavior

`./experiments/start` should:

1. Prompt for a short experiment name.
2. Normalize it into a filesystem-friendly suffix.
3. Create `experiments/YYYY-MM-DD_name/`.
4. Copy the experiment `AGENTS.md` and `README.md` templates from `agent-workflow/` into the new experiment root.
5. Copy `TODO_GUIDE.md` and `TODO_TEMPLATE.md` from `agent-workflow/` into the new experiment root.
6. Copy `runner_template.sh` into the new experiment as `runner.sh`.
7. Create `runner_lib/`, `configs/`, `results/`, and `logs/` inside it.
8. Refuse to overwrite an existing experiment directory.
9. Keep the default setup directly in `runner.sh` and use `runner_lib/` only when extra helper files are needed later.
