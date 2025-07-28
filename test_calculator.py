import pytest
from calculator import add, sub, mul, div, power, sqrt


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 4) == -4
    assert sub(-1, 1) == -2


def test_mul():
    assert mul(5, 3) == 15
    assert mul(-2, 4) == -8
    assert mul(0, 5) == 0


def test_div():
    assert div(15, 3) == 5
    assert div(50, 2) == 25
    assert div(0, 2) == 0


def test_div_zero():
    with pytest.raises(ValueError):
        div(10, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(0, 0) == 1
    assert power(0, 1) == 0


def test_sqrt():
    assert sqrt(4) == 2
    assert sqrt(0) == 0
    assert sqrt(9) == 3
    with pytest.raises(ValueError):
        sqrt(-1)
