import logging

x, y = map(int, input('Введите два целых числа через пробел: ').split())


def log_deco(func):
    def wrapper(a, b):
        try:
            logging.info(f'Result: {a} / {b} = {func(a, b)}')
        except ZeroDivisionError:
            logging.error('ZeroDivisionZero')

    return wrapper


@log_deco
def log_div(c, d):
    return c / d


log_div(x, y)
