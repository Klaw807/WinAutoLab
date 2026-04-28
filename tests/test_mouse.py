import importlib.util
from pathlib import Path

from winautolab.mouse import ClickPoint, build_click_batch, to_absolute


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "run_mouse_clicks.py"
SPEC = importlib.util.spec_from_file_location("run_mouse_clicks", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
run_mouse_clicks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(run_mouse_clicks)


def test_to_absolute_uses_sendinput_coordinate_space():
    assert to_absolute(960, 540, 1920, 1080) == (32767, 32767)


def test_build_click_batch_creates_move_down_up_per_point():
    batch = build_click_batch([ClickPoint(10, 20), ClickPoint(30, 40)], 1920, 1080)
    assert len(batch) == 6


def test_run_mouse_clicks_parser_uses_default_points_file():
    parser = run_mouse_clicks.build_parser()
    args = parser.parse_args([])
    assert Path(args.points_file) == run_mouse_clicks.DEFAULT_POINTS_FILE
