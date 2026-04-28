# T001 Migrate Legacy Automation Logic

- linked task: `T001`
- status: `TODO.md` is the source of truth for task status
- created date: `2026-04-28`
- last updated date: `2026-04-28`

## Goal

Migrate the useful automation logic from `C:\Users\yangyx\OneDrive\01_working\16_code_[B]` into this repository's project-owned structure without modifying the source directory.

## Scope

- move reusable Windows mouse automation logic into `src/`
- add a project-specific runnable entrypoint in `scripts/`
- migrate mouse coordinate capture into a small reusable helper
- migrate the HTML image download helper into reusable code
- replace hardcoded browser automation script details with config-driven scaffolding
- add focused tests for pure logic
- update docs for the new entrypoints and structure

## Source Inventory

- `mouse_multi_press.py`: scheduled multi-point Windows click batch automation with preview overlay
- `mouse_detect.py`: print current mouse position after a short delay
- `jpg.py`: download all page images into a folder
- `help_submit.py`: one-off Selenium browser automation with hardcoded secrets and site-specific selectors
- `badminton.txt`: browser console helper snippet related to the form automation

## Migration Approach

1. Create reusable modules under `src/`
2. Expose small scripts under `scripts/` for the migrated workflows
3. Keep the browser automation safe by moving it to a config/template pattern instead of preserving secrets
4. Add tests for pure helpers and structure-sensitive logic
5. Update `README.md` so the current repo clearly replaces the old ad hoc folder

## Open Decisions

- preserve the legacy browser automation intent, but do not migrate embedded credentials
- prefer JSON-based point/config input so the repo can hold repeatable automation definitions

## History Log

- `2026-04-28` created plan and linked it from `TODO.md`
