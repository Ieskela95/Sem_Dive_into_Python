list_el = [2, 99, 7.4, "Print", True]
for i in range(len(list_el)):
    print(i + 1, end=" | ")
    print("Значение -> ",list_el[i], end=" | ")
    print("Адрес в оперативной памяти ", id(list_el[i]), end=" | ")
    print("Размер", list_el[i].__sizeof__(), end=" | ")
    print("hash = ",hash(list_el[i]), end=" | ")
    print("является числом" if isinstance(list_el[i], int) else "не является целым числом", end=" | ")
    print("является строкой" if isinstance(list_el[i], str) else "не является строкой")
    print("*" * 150)