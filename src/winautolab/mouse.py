import ctypes
import json
import time
from ctypes import wintypes
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Sequence

try:
    import tkinter as tk
except ImportError:  # pragma: no cover - tkinter availability is environment-specific
    tk = None


@dataclass(frozen=True)
class ClickPoint:
    x: int
    y: int


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ctypes.c_ulonglong),
    ]


class INPUT(ctypes.Structure):
    _fields_ = [
        ("type", wintypes.DWORD),
        ("mi", MOUSEINPUT),
    ]


MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_VIRTUALDESK = 0x4000


def enable_dpi_awareness() -> None:
    """Prefer physical-pixel coordinates so capture and playback match on scaled displays."""
    user32 = ctypes.windll.user32
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
        return
    except (AttributeError, OSError):
        pass

    try:
        user32.SetProcessDPIAware()
    except (AttributeError, OSError):
        pass


def load_points_from_json(path: str | Path) -> list[ClickPoint]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    raw_points = data["points"] if isinstance(data, dict) else data
    return [ClickPoint(int(point[0]), int(point[1])) for point in raw_points]


def to_absolute(x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
    """Convert screen coordinates to the absolute SendInput coordinate space."""
    if screen_width <= 1 or screen_height <= 1:
        raise ValueError("screen dimensions must be greater than 1 pixel")
    abs_x = round(x * 65535 / (screen_width - 1))
    abs_y = round(y * 65535 / (screen_height - 1))
    return abs_x, abs_y


def preview_points(points: Sequence[ClickPoint], duration_ms: int | None = None) -> None:
    if tk is None:
        raise RuntimeError("tkinter is required for preview mode")

    enable_dpi_awareness()
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.35)
    root.configure(bg="black")
    try:
        root.tk.call("tk", "scaling", 1.0)
    except tk.TclError:
        pass

    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    marker_radius = 24
    index_font = ("Arial", 24, "bold")
    coordinate_font = ("Arial", 14)
    coordinate_offset = 46
    header_font = ("Arial", 20, "bold")

    for idx, point in enumerate(points, start=1):
        canvas.create_oval(
            point.x - marker_radius,
            point.y - marker_radius,
            point.x + marker_radius,
            point.y + marker_radius,
            outline="red",
            width=4,
        )
        canvas.create_text(
            point.x,
            point.y,
            text=str(idx),
            fill="white",
            font=index_font,
        )
        canvas.create_text(
            point.x,
            point.y + coordinate_offset,
            text=f"({point.x}, {point.y})",
            fill="yellow",
            font=coordinate_font,
        )

    canvas.create_text(
        30,
        30,
        anchor="nw",
        text="Preview mode: red circles are click points. Press Esc or click to continue.",
        fill="white",
        font=header_font,
    )

    root.bind("<Escape>", lambda event: root.destroy())
    root.bind("<Button-1>", lambda event: root.destroy())
    if duration_ms is not None:
        root.after(duration_ms, root.destroy)
    root.mainloop()


def build_click_batch(
    points: Iterable[ClickPoint], screen_width: int, screen_height: int
) -> ctypes.Array:
    events: list[INPUT] = []
    for point in points:
        abs_x, abs_y = to_absolute(point.x, point.y, screen_width, screen_height)
        events.append(
            INPUT(
                type=0,
                mi=MOUSEINPUT(
                    abs_x,
                    abs_y,
                    0,
                    MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_VIRTUALDESK,
                    0,
                    0,
                ),
            )
        )
        events.append(
            INPUT(
                type=0,
                mi=MOUSEINPUT(abs_x, abs_y, 0, MOUSEEVENTF_LEFTDOWN, 0, 0),
            )
        )
        events.append(
            INPUT(
                type=0,
                mi=MOUSEINPUT(abs_x, abs_y, 0, MOUSEEVENTF_LEFTUP, 0, 0),
            )
        )
    return (INPUT * len(events))(*events)


def send_click_batch(batch: ctypes.Array) -> None:
    send_input = ctypes.windll.user32.SendInput
    sent = send_input(len(batch), batch, ctypes.sizeof(INPUT))
    if sent == 0:
        raise ctypes.WinError()


def get_screen_size() -> tuple[int, int]:
    enable_dpi_awareness()
    user32 = ctypes.windll.user32
    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def get_cursor_position() -> ClickPoint:
    enable_dpi_awareness()
    point = wintypes.POINT()
    if not ctypes.windll.user32.GetCursorPos(ctypes.byref(point)):
        raise ctypes.WinError()
    return ClickPoint(point.x, point.y)


def run_scheduled_clicks(
    points: Sequence[ClickPoint],
    target_time: str,
    repeat_count: int = 3,
    repeat_interval_seconds: float = 0.02,
    poll_interval_seconds: float = 0.001,
    preview: bool = True,
) -> None:
    if preview:
        preview_points(points)

    screen_width, screen_height = get_screen_size()
    batch = build_click_batch(points, screen_width, screen_height)
    print(f"Built click batch for {len(points)} points. Waiting for {target_time}...")

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == target_time:
            for index in range(repeat_count):
                send_click_batch(batch)
                if index < repeat_count - 1:
                    time.sleep(repeat_interval_seconds)
            print(f"Triggered clicks at {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
            return
        time.sleep(poll_interval_seconds)
