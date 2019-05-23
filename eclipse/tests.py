import pytest
from click import BadParameter
from click.testing import CliRunner

from eclipse import Line, cli, input_to_line, is_overlapping


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


def test_is_overlapping_partial_x1_gt_x2():
    line_a = Line(5, 1)
    line_b = Line(6, 3)

    assert is_overlapping(line_a, line_b) is True


def test_input_to_line_success():
    assert input_to_line('1, 2') == Line(1, 2)


def test_input_to_line_type_error():
    with pytest.raises(BadParameter):
        input_to_line('1') == Line(1, 2)


def test_input_to_line_value_error():
    with pytest.raises(BadParameter):
        input_to_line('1, a') == Line(1, 2)


def test_cli_execution_do_overlap():
    runner = CliRunner()
    result = runner.invoke(cli, input='1,2\n2,3')

    assert result.exit_code == 0
    assert 'do overlap' in result.output


def test_cli_execution_do_not_overlap():
    runner = CliRunner()
    result = runner.invoke(cli, input='1,2\n3,4')

    assert result.exit_code == 0
    assert 'do not overlap' in result.output
