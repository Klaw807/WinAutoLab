# WinAutoLab

Project-owned workspace for Windows automation scripts, mouse/input simulation, web or data scraping, and temporary script experiments.

Examples:

- Shanghaitech badminton form autofill
- Browser-side JavaScript helpers
- Mouse click or keyboard simulation
- Small one-off automation prototypes before they graduate into reusable code

## Structure

```text
WinAutoLab/
|- src/                # project-owned implementation
|- tests/              # tests for project-owned code
|- scripts/            # project-specific automation entrypoints
|- configs/            # checked-in project configuration
|- repos/              # upstream, external, forked, or submodule code only
|- experiments/        # temporary experiments and run outputs
|- toolkit/            # reusable cross-project utilities
|- agent-workflow/     # shared workflow rules and TODO scaffolding
|- docs/plans/         # larger local implementation plans and history
```

## Working Rules

- Put new project code in `src/`
- Put tests for that code in `tests/`
- Put project-only automation helpers in `scripts/`
- Put checked-in configuration in `configs/`
- Keep reusable shared utilities in `toolkit/`
- Keep `repos/` reserved for code that is owned elsewhere

## Notes

- Use `TODO.md` as the live control plane for current tasks
- Use `docs/plans/` only when a task needs a larger implementation plan
- Keep docs short and update them when the workspace behavior changes
