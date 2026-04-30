# T011 Add Real Click-Emulation Verification Test

- linked task: `T011`
- status: `done`
- created date: `2026-04-30`
- closed date: `2026-04-30`
- last updated date: `2026-04-30`

## Summary

Added an opt-in manual integration test that verifies `run_scheduled_clicks` can trigger a real UI button through emitted mouse input on Windows.

## Outcome

- extended `tests/test_mouse.py` with a manual Tkinter-based real click test
- added `pytest.ini` marker metadata for manual interaction tests
- preserved the default automated path by skipping the real click test unless explicitly enabled

## History Log

- `2026-04-30` added a manual Windows-only test that opens a topmost Tkinter window, targets the button center, and asserts the scheduled click activates it
- `2026-04-30` verified the non-manual mouse tests with `pytest tests\\test_mouse.py -m "not manual"`

## Notes

- run the real test with `WINAUTOLAB_RUN_REAL_CLICK_TEST=1`
- the test moves and clicks the physical mouse, so it is intentionally opt-in
