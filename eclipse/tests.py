from eclipse import Line, is_overlapping


def test_line_creation():
    line = Line(1, 2)

    assert line.x1 == 1
    assert line.x2 == 2


def test_is_overlapping_not_overlap():
    line_a = Line(1, 2)
    line_b = Line(3, 5)

    assert is_overlapping(line_a, line_b) is False


def test_is_overlapping_partial_a_right():
    line_a = Line(1, 3)
    line_b = Line(2, 5)

    assert is_overlapping(line_a, line_b) is True


def test_is_overlapping_partial_a_left():
    line_a = Line(2, 5)
    line_b = Line(1, 3)

    assert is_overlapping(line_a, line_b) is True


def test_is_overlapping_partial_a_inside_b():
    line_a = Line(2, 3)
    line_b = Line(1, 5)

    assert is_overlapping(line_a, line_b) is True


def test_is_overlapping_partial_b_inside_a():
    line_a = Line(1, 5)
    line_b = Line(2, 4)

    assert is_overlapping(line_a, line_b) is True


def test_is_overlapping_negative_number():
    line_a = Line(-5, -3)
    line_b = Line(-4, -1)

    assert is_overlapping(line_a, line_b) is True


def test_is_overlapping_decimal_number():
    line_a = Line(1.2, 4.6)
    line_b = Line(2.2, 7.8)

    assert is_overlapping(line_a, line_b) is True
