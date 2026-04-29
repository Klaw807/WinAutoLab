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

## Docs

- `docs/badminton_js_script.txt`: copy-paste JavaScript for the Chrome DevTools console to help prefill the Shanghaitech badminton form

## Script Guides

### Download Videos From Links

`scripts/download_videos_from_link.py` downloads one or more direct video or `.m3u8` links with `ffmpeg`.

How to use:

1. Install `ffmpeg` and make sure `ffmpeg` works in your terminal.
2. Open `scripts/download_videos_from_link.py`.
3. Add one or more video URLs into the `links = []` list at the bottom of the file.
4. Run `python scripts/download_videos_from_link.py` from the workspace root.

Behavior:

- each link is downloaded with `ffmpeg -i "<link>" -c copy`
- output files are named like `video_YYYYMMDDHHMMSS.mp4`
- files are written to the current working directory where you run the command

Example:

```python
links = [
    "https://example.com/video.m3u8",
]
```

## Automation Entry Points

- `python scripts/run_mouse_clicks.py --time 12:00:00`
- `python scripts/run_mouse_clicks.py configs/mouse_points.example.json --time 12:00:00`
- `python scripts/show_mouse_position.py --delay 3`
- `python scripts/download_page_images.py https://example.com/page --output downloaded_images`
- `python scripts/download_videos_from_link.py`
- `python scripts/run_browser_workflow.py configs/browser_workflow.example.json`

## Python Dependencies

- mouse position helper: `pyautogui`
- image downloader: `requests`
- video downloader: `ffmpeg` available on `PATH`
- browser workflow runner: `selenium`
