"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

n_col = 5
n_row = 4
# создаем исходную матрицу и заполняем ее случайными значениями
matrix = [[random.randint(0, 100) for _ in range(n_col)] for _ in range(n_row)]

min_lst = []  # создаем пустой список, в котором будут минимальные элементы колонок матрицы
max_num = 0  # присваиваем начальное значение переменной
for col in range(n_col):  # организуем цикл по колонкам
    min_pos = 0
    for i in range(n_row):  # цикл по строкам одной колонки
        if matrix[i][col] < matrix[min_pos][col]:
            min_pos = i
    min_lst.append(matrix[min_pos][col])  # наполняем список минимальными значениями колонок.
    if matrix[min_pos][col] > max_num:  # вычисляем сразу максимальное значение
        max_num = matrix[min_pos][col]

# выводим на печать исходную матрицу
for line in matrix:
    for item in line:
        print(f'{item:>5}', end='')
    print()

# Выводим на печать минимальные значения в колонках и максимальное значение среди них.
print(f'{"-" * 5 * n_col}')
for i in min_lst:
    print(f'{i:>5}', end='')
print(f' Max value: {max_num}')
