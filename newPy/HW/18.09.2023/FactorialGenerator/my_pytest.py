import pytest
from task_new import FatorialGenerator


def test_fatorial_generator_with_one_argument():
    gen = FatorialGenerator(5)
    result = list(gen)
    assert result == [1, 2, 6, 24, 120]


def test_fatorial_generator_with_two_arguments():
    gen = FatorialGenerator(2, 4)
    result = list(gen)
    assert result == [2, 6]


def test_fatorial_generator_with_three_arguments():
    gen = FatorialGenerator(1, 5, 2)
    result = list(gen)
    assert result == [1, 6, 120]


def test_empty_fatorial_generator():
    gen = FatorialGenerator()
    result = list(gen)
    assert result == []


if __name__ == '__main__':
    pytest.main()
