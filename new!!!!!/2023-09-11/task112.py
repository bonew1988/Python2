# Создайте функцию,
# которая удаляет из текста все
# символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters, punctuation


def clean_text(text: str) -> str:
    """A function that removes characters from text other than Latin letters and spaces.
        >>> clean_text('Some text, тест')
        'some text, '

        >>> clean_text('Hell456o worущшуd!')
        'hello word!'

        >>> clean_text('У меня есть подруга Anna! Ей 21 год.')
        '    anna!   .'
        """

    return "".join(i for i in text
                   if i in ascii_letters + punctuation + " ").lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
