# Напишите функцию принимающую на вход только ключевые параметры и возвращающую
# словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

from typing import Any, Dict, Union, Tuple


def create_argument_dict(**kwargs: Any) -> Dict[Union[int, float, str, bool, Tuple, str], Any]:
    argument_dict = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, bool, Tuple)):
            argument_dict[key] = value
        else:
            argument_dict[str(key)] = value
    return argument_dict


result = create_argument_dict(
    a=1, b=2, c="hello world", d=(3, 4), e=False, f=3.14, g=[1, 2])
print(result)
