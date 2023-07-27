# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ
# — значение переданного аргумента, а значение — имя аргумента. Если ключ не хэшируем,
# используйте его строковое представление.
def task_2(**kwargs):
    dict_res = {}
    for key, value in kwargs.items():
        if isinstance(value, dict | list | set):
            dict_res[str(value)] = key
        else:
            dict_res[value] = key
    return dict_res


res = task_2(one=True, two={"one", 1}, three=3, my_set={1, 1, 1, 2, 3})
print(res)
