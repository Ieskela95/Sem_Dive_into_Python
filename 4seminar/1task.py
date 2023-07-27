# Напишите функцию для транспонирования матрицы
matrix1 = [[3, 5, 6, 0],
            [1, 4, 6, 2]]
print("Дана матрица: \n" + '\n'.join(list(map(str, matrix1))))

print("транспонированная матрица (решение в одну строку с красивым выводом):\
 \n"+'\n'.join(list(map(str, [list(line) for line in zip(*matrix1)]))))


def transpose(matrix):

    res = []
    row = len(matrix)
    colum = len(matrix[0])
    for j in range(colum):
        tmp = []
        for i in range(row):
            tmp = tmp + [matrix[i][j]]
        res = res + [tmp]
    return res

print("Транспонированная матрица: \n"+'\n'.join(list(map(str, transpose(matrix1)))))
