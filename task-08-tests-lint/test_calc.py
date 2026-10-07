import pytest

from calc import add, divide, is_even


def test_add():
    assert add(2, 4) == 6


assert add(-1, 1) == 0
assert add(0, 0) == 0


def test_divide():
    assert divide(10, 2) == 5.0


assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide"):
        divide(10, 0)


@pytest.mark.parametrize(
    "n,expected",
    [
        (2, True),
        (3, False),
        (0, True),
        (-4, True),
        (-5, False),
    ],
)
def test_is_even(n: int, expected: bool):
    assert is_even(n) == expected
