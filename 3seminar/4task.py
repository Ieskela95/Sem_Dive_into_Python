# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
def pack_backpack(items, max_heft):
    possible_items = []
    for item, heft in items.items():
        if heft <= max_heft:
            possible_items.append(item)
            max_heft -= heft
    return possible_items

max_heft = int(input('Введите максимальную грузоподъёмность рюкзака -> '))
items = {'Палатка': 5, 'Вода': 3, 'Еда': 4, 'Одежда': 2, 'Аптечка': 1}
print(f"В рюкзаке: ", ", ".join(pack_backpack(items, max_heft)))
