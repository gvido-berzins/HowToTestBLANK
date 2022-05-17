import pytest


def validate_string(value: str) -> bool:
    """Validation function with the generic Exception"""
    if isinstance(value, str) and len(value) > 0:
        return True
    else:
        raise Exception(f"Invalid value given '{value}', expected a non-empty string")


def parse_line(line: str, sep: str = " ") -> tuple[int]:
    """Parse given line into a tuple of integers"""
    if not line:
        return tuple()

    def from_int(x: str) -> int:
        return int(x)

    if isinstance(line, str):
        tuples = tuple(from_int(x) for x in line.strip().split(sep) if x)
        return tuples
    return tuple()


@pytest.mark.parametrize(
    ("line", "expected"),
    (
        ("1 2", (1, 2)),
        (" 1  2", (1, 2)),
        ("1  2 1   2", (1, 2, 1, 2)),
        (None, tuple()),
    ),
)
def test_parse_line_returns_numbers(line, expected):
    int_tuple = parse_line(line)
    assert int_tuple == expected


@pytest.mark.parametrize("line", ("a", "\x08", "\u0001"))
def test_parse_line_invalid_case_exception(line):
    pytest.raises(ValueError, parse_line, line)


@pytest.mark.parametrize("line", ("a", "\x08", "\u0001"))
def test_parse_line_invalid_case_exception_second_style(line):
    with pytest.raises(ValueError):
        parse_line(line)


@pytest.mark.parametrize("value", (int, 1, None, (), dict(), "", [1, 2]))
def test_validate_string(value):
    with pytest.raises(Exception, match=r"Invalid.*non-empty string"):
        validate_string(value)
