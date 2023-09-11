import pytest
from task112 import clean_text


def test_one_clean_text():
    assert clean_text(
        'Some text, тест') == 'some text, ', 'Тест один не пройден !'


def test_two_clean_text():
    assert clean_text(
        'Hell456o worущшуd!') == 'hello word!', 'Тест два не пройден !'


def test_three_clean_text():
    assert clean_text(
        'У меня есть подруга Anna! Ей 21 год.') == '    anna!   .', 'Тест три не пройден'


if __name__ == '__main__':
    pytest.main()
