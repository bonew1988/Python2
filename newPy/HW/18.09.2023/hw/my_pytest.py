import pytest
from my_task import Rectangle


def test_calc_len():
    r = Rectangle(3, 4)
    assert r.calc_len() == 14


def test_calc_square():
    r = Rectangle(3, 4)
    assert r.calc_square() == 12


def test_addition():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(5, 2)
    r3 = r1 + r2
    assert r3.calc_len() == 16
    assert r3.calc_square() == 20


def test_subtraction():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(2, 2)
    r3 = r1 - r2
    assert r3.calc_len() == 10
    assert r3.calc_square() == 10


def test_comparison():
    r1 = Rectangle(3, 4)
    r2 = Rectangle(2, 5)
    assert r1 == r1
    assert r1 != r2
    assert r1 < r2
    assert r1 <= r2
    assert r2 > r1
    assert r2 >= r1


if __name__ == '__main__':
    pytest.main()
