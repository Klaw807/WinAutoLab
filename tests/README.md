# Tests Guide

This folder contains focused tests for the project-owned code in `src/` and for a few script entrypoint behaviors.

## How To Run

Run the full default test suite from the workspace root:

```powershell
pytest
```

Run only the mouse tests:

```powershell
pytest tests\test_mouse.py
```

Run only the non-manual mouse tests:

```powershell
pytest tests\test_mouse.py -m "not manual"
```

Run the real click-emulation test on Windows:

```powershell
$env:WINAUTOLAB_RUN_REAL_CLICK_TEST = "1"
pytest tests\test_mouse.py -k real_button_click -s
```

Notes for the manual mouse test:

- it is Windows-only
- it loads points from `configs/mouse_points.json`
- it opens a topmost full-screen Tkinter window with clickable targets placed at those exact coordinates
- it moves and clicks the physical mouse
- keep your desktop clear and do not touch the mouse while it runs
- if one of the configured points is outside the current screen resolution, the test is skipped
- if `WINAUTOLAB_RUN_REAL_CLICK_TEST` is not set to `1`, the test is skipped on purpose

## Test Logic

### `tests/test_mouse.py`

This file covers the mouse automation helpers and the `scripts/run_mouse_clicks.py` CLI wiring.

- `test_to_absolute_uses_sendinput_coordinate_space`
  checks that screen origin `(0, 0)` maps to the `SendInput` absolute origin `(0, 0)`
- `test_to_absolute_maps_bottom_right_to_sendinput_max`
  checks that the bottom-right pixel maps to the maximum `SendInput` range `(65535, 65535)`
- `test_build_click_batch_creates_move_down_up_per_point`
  checks that each click point becomes three low-level mouse events: move, left-down, and left-up
- `test_run_mouse_clicks_parser_uses_default_points_file`
  checks that the CLI script uses `configs/mouse_points.json` when no points file is passed
- `test_run_scheduled_clicks_can_trigger_a_real_button_click`
  is an opt-in integration test that loads `configs/mouse_points.json`, places one real Tkinter button at each configured coordinate, schedules the clicks for those exact points, and passes only if every target button callback is triggered

### `tests/test_browser_forms.py`

This file validates workflow configuration loading for browser automation.

- writes a temporary JSON config file
- loads it with `load_workflow(...)`
- checks that important fields such as `start_url`, `post_login_urls`, and `actions` are preserved correctly

### `tests/test_image_download.py`

This file validates small helper behaviors used by the image downloader.

- `test_clean_filename_removes_windows_invalid_characters`
  checks that Windows-invalid path characters are removed
- `test_extract_image_urls_resolves_relative_and_absolute_paths`
  checks that relative image paths are resolved against the page URL and absolute URLs are kept
- `test_filename_from_url_uses_url_path_basename`
  checks that the output filename comes from the final URL path segment instead of query parameters

## Why The Mouse Tests Are Split

Most mouse tests are safe unit tests that verify coordinate conversion, event-batch structure, and CLI defaults without touching the real cursor.

The manual test exists separately because it answers a different question: not just whether the code builds the right event structures, but whether Windows actually delivers the emitted click to a real UI control.
