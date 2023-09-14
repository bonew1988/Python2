# На семинаре про декораторы был создан
# логирующий декоратор. Он сохранял
# аргументы функции и результат её
# работы в файл. Напишите аналогичный
# декоратор, но внутри используйте
# модуль logging
import logging
from functools import wraps

FORMAT = \
    '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'

logging.basicConfig(format=FORMAT,
                    style='{',
                    filename="log_for_tast3.log",
                    encoding='utf-8',
                    level=logging.ERROR,
                    filemode='a')

logger = logging.getLogger(__name__)


def deco(func: callable):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except Exception as message_errors:
            logger.error(f'Функция {func.__name__} '
                         f'с аргументами {args = }, '
                         f'{kwargs =} выдвала ошибку: '
                         f'{message_errors = }')
            return None

    return wrapper


@deco
def div(a, b):
    return a/b


if __name__ == '__main__':
    div(1, 0)
