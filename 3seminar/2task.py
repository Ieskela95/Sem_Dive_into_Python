# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 2, 1, 6, 6, 4, 5, 8, 1, 1, 5, 7, 8, 9, 9, 5, 5, 4]
duplicates = []
i = 0

while i < len(my_list):
    if my_list.count(my_list[i]) > 1:
        for _ in range(1, (my_list.count(my_list[i]))):
            duplicates.append(my_list.pop(my_list.index(my_list[i], i + 1)))

    i += 1

print(f"Дубликаты:             {duplicates}")
print(f"Результирующий список: {my_list}")
