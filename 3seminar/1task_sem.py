from pprint import pprint
from random import randint
from collections import Counter

input_u = input("Введите -> ")
if input_u.isdigit():
    print(" Целое = ", int(input_u))
elif any(i.isupper() for i in input_u):
    print(" Есть заглавная, \n  делаем в нижнем регистре: ", input_u.lower())
elif input_u.islower():
    print("Строка в нижнем регистре: ", input_u.lower())
elif isinstance(float(input_u), float):
    print(" Вещественное = ", float(input_u))

my_tuple = (True, "String", 2, False, 5.16, 4-3j, [1, 4, 5], (3, 4, 6), {2, 5, 5, 7, 6}, {4, 7, 6}, 43, 'second')

result_dict = {}

for i in my_tuple:
    if type(i).__name__ not in result_dict:
        result_dict[type(i).__name__] = []
    result_dict[type(i).__name__].append(i)

pprint(result_dict)


a = randint(5, 10)
b = []
for i in range(a):
    b.append(randint(1, 9))
print(b)
c = []
for i in b:
    if b.count(i) == 1:
        c.append(i)
print(c)

my_list = [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9]

result = []


for i in range(len(my_list)):
    if my_list[i] % 2:
        result.append(i + 1)

print(*result)

print(my_list := [2, 3, 4, 4, 4, 2, 5, 7, 6, 7, 8, 9, 6, 9])

print(*[i + 1 for i in range(len(my_list)) if my_list[i] % 2])


words = input('Введите предложение >>> ').split()

max_len = len(max(words, key=len))

for i in range(len(sorted(words))):
    print(f"{i+1}.{words[i].rjust(max_len+1)}")


obj = input('Введите строку >>> ')

result1 = {}
result2 = {}
result3 = Counter(obj)
result4 = {}

for i in obj:
    result1[i] = result1.setdefault(i, 0) + 1

for i in obj:
    if i not in result2:
        result2[i] = obj.count(i)

for i in obj:
    if i not in result4:
        result4[i] = 0
    result4[i] += 1

print(result1, result2, result4, result3, sep='\n')
