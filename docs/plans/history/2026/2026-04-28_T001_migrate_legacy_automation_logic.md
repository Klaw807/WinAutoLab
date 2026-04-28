# T001 Migrate Legacy Automation Logic

- linked task: `T001`
- status: `done`
- created date: `2026-04-28`
- closed date: `2026-04-28`
- last updated date: `2026-04-28`

## Summary

Migrated the useful logic from the legacy `16_code_[B]` folder into project-owned modules and scripts in this repository without modifying the source folder.

## Outcome

- added reusable automation modules in `src/winautolab/`
- added runnable scripts for scheduled mouse clicks, cursor position capture, image download, and config-driven browser workflows
- added example config files under `configs/`
- added tests for pure logic and config loading
- updated `README.md` to position this repo as the maintained home for the legacy automation use cases

## History Log

- `2026-04-28` reviewed workspace workflow docs and source repo inventory before making changes
- `2026-04-28` created the active task entry and migration plan
- `2026-04-28` migrated mouse automation, image download, and browser workflow scaffolding into `src/` and `scripts/`
- `2026-04-28` added tests and example configs
- `2026-04-28` verified the migration with `python -m pytest tests`

## Notes

- the source directory `C:\Users\yangyx\OneDrive\01_working\16_code_[B]` was used as read-only reference
- the legacy Selenium script had embedded credentials, so the maintained version intentionally uses config placeholders instead

