"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random


def merge_sort(array, fst, lst):  # разбиваем массив рекурсивно методом половиннного деления до одномерных массивов

    if lst - fst > 1:
        mid = (fst + lst)//2
        merge_sort(array, fst, mid)
        merge_sort(array, mid, lst)
        merge_list(array, fst, mid, lst)


def merge_list(array, fst, mid, lst):  # собираем массив из одномерных попарно, одновременно сортируя элементы
    # в том числе из ждвух массивов
    left = array[fst:mid]
    right = array[mid:lst]
    k = fst
    i = 0
    j = 0
    while (fst + i < mid and mid + j < lst):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if fst + i < mid:
        while k < lst:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < lst:
            array[k] = right[j]
            j = j + 1
            k = k + 1


size = 5
array = [random.uniform(0, 50) for _ in range(size)]
print('Исходный массив:')
print(array)
merge_sort(array, 0, len(array))
print('Отсортированный массив:')
print(array)
