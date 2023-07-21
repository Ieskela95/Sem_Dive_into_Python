select_s = int(input("Введите систему счисления (2 - 8)-> "))
res = ""
n = int(input("Введите число: "))
n1 = n
while n > 0:
    res = str(n % select_s) + res
    n = n // select_s
print(f"Ваше число в {select_s}-ной системе счисления = ", res)
# проверка
print(bin(n1)[2:] if select_s == 2 else (oct(n1)[2:] if select_s == 8 else "вы не выбрали 2 или 8"))
