from winautolab.mouse import ClickPoint, build_click_batch, to_absolute


def test_to_absolute_uses_sendinput_coordinate_space():
    assert to_absolute(960, 540, 1920, 1080) == (32767, 32767)


def test_build_click_batch_creates_move_down_up_per_point():
    batch = build_click_batch([ClickPoint(10, 20), ClickPoint(30, 40)], 1920, 1080)
    assert len(batch) == 6

