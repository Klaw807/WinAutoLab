import importlib.util
import os
import sys
import threading
import time
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from winautolab.mouse import ClickPoint, build_click_batch, get_screen_size, load_points_from_json, run_scheduled_clicks, to_absolute


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "run_mouse_clicks.py"
SPEC = importlib.util.spec_from_file_location("run_mouse_clicks", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
run_mouse_clicks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(run_mouse_clicks)


def test_to_absolute_uses_sendinput_coordinate_space():
    assert to_absolute(0, 0, 1920, 1080) == (0, 0)


def test_to_absolute_maps_bottom_right_to_sendinput_max():
    assert to_absolute(1919, 1079, 1920, 1080) == (65535, 65535)


def test_build_click_batch_creates_move_down_up_per_point():
    batch = build_click_batch([ClickPoint(10, 20), ClickPoint(30, 40)], 1920, 1080)
    assert len(batch) == 6


def test_run_mouse_clicks_parser_uses_default_points_file():
    parser = run_mouse_clicks.build_parser()
    args = parser.parse_args([])
    assert Path(args.points_file) == run_mouse_clicks.DEFAULT_POINTS_FILE


@pytest.mark.manual
@pytest.mark.skipif(sys.platform != "win32", reason="real click test requires Windows")
def test_run_scheduled_clicks_can_trigger_a_real_button_click():
    if os.environ.get("WINAUTOLAB_RUN_REAL_CLICK_TEST") != "1":
        pytest.skip("Set WINAUTOLAB_RUN_REAL_CLICK_TEST=1 to allow a real mouse click test.")

    tkinter = pytest.importorskip("tkinter")
    points = load_points_from_json(run_mouse_clicks.DEFAULT_POINTS_FILE)
    screen_width, screen_height = get_screen_size()
    for point in points:
        if point.x >= screen_width or point.y >= screen_height:
            pytest.skip(
                f"Configured point ({point.x}, {point.y}) is outside the current screen {screen_width}x{screen_height}."
            )

    clicked: set[int] = set()
    worker_errors: list[BaseException] = []

    root = tkinter.Tk()
    root.title("WinAutoLab Click Test")
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.configure(bg="black")

    try:
        root.update_idletasks()
        root.lift()
        root.focus_force()

        buttons = []
        target_size = 72
        for index, point in enumerate(points):
            button = tkinter.Button(root, text=str(index + 1), command=lambda idx=index: clicked.add(idx))
            button.place(
                x=max(0, point.x - root.winfo_rootx() - (target_size // 2)),
                y=max(0, point.y - root.winfo_rooty() - (target_size // 2)),
                width=target_size,
                height=target_size,
            )
            buttons.append(button)

        root.update()
        target_time = (datetime.now() + timedelta(seconds=2)).strftime("%H:%M:%S")

        def worker() -> None:
            try:
                run_scheduled_clicks(
                    points,
                    target_time=target_time,
                    repeat_count=1,
                    repeat_interval_seconds=0.0,
                    poll_interval_seconds=0.001,
                    preview=False,
                )
            except BaseException as exc:  # pragma: no cover - only exercised on failure
                worker_errors.append(exc)

        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

        deadline = time.time() + 6
        while time.time() < deadline and len(clicked) < len(points) and not worker_errors:
            root.update()
            time.sleep(0.01)

        thread.join(timeout=1)
    finally:
        root.destroy()

    if worker_errors:
        raise worker_errors[0]

    assert len(clicked) == len(points), "The scheduled clicks did not activate all configured target buttons."
