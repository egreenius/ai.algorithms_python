"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""

import random


def buble_sort_desc(array):  # базовый алгоритм сортировки, возвращает кортеж с количеством внешнего и внутреннего цикла
    n = 1
    count = 0
    while n < len(array):

        for i in range(len(array) - 1, -1 + n, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
            count += 1
        n += 1
    return n, count


def test_buble_sort_desc(size):  # функция тестирования базового алгоритма для командной строки
    array = [random.randint(-100, 100) for _ in range(size)]
    buble_sort_desc(array)

# python3 -m timeit -n 10 -s "import les_7_hw_1" "les_7_hw_1.test_buble_sort_desc(10)"
# 10 loops, best of 5: 21.4 usec per loop
# python3 -m timeit -n 10 -s "import les_7_hw_1" "les_7_hw_1.test_buble_sort_desc(100)"
# 10 loops, best of 5: 1.03 msec per loop
# python3 -m timeit -n 10 -s "import les_7_hw_1" "les_7_hw_1.test_buble_sort_desc(500)"
# 10 loops, best of 5: 26.6 msec per loop


def buble_sort_desc_new(array):  # убираем лишние циклы, в случае, если массив уже оказался отсортирован
    n = 1
    sorted = False
    count = 0
    while n < len(array) and not sorted:
        sorted = True  # если нет ни одного перемещения во внутреннем цикле, то массив отсортирован
        for i in range(len(array) - 1, -1 + n, -1):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                sorted = False
            count += 1
        n += 1
    return n, count


def test_buble_sort_desc_new(size):  # функция для тестирования усовершенствованного алгоритма
    array = [random.randint(-100, 100) for _ in range(size)]
    buble_sort_desc_new(array)

# python3 -m timeit -n 10 -s "import les_7_hw_1" "les_7_hw_1.test_buble_sort_desc_new(10)"
# 10 loops, best of 5: 20.6 usec per loop
# python3 -m timeit -n 10 -s "import les_7_hw_1" "les_7_hw_1.test_buble_sort_desc_new(100)"
# 10 loops, best of 5: 996 usec per loop
# python3 -m timeit -n 10 -s "import les_7_hw_1" "les_7_hw_1.test_buble_sort_desc_new(500)"
# 10 loops, best of 5: 26.5 msec per loop


def buble_sort_new(array):  # функция, учитывающая "слипшиеся" пузырьки. Сортировка по возрастанию
    n = 1
    sorted = False
    count = 0
    count_in = 0
    while n < len(array) and not sorted:
        sorted = True
        j = 0
        glue = 1
        for i in range(len(array) - n):
            count_in += 1
            if array[i] > array[i + 1]:
                if j < i and not sorted:
                    glue += 1
                for k in range(glue):
                    if array[i - k] > array[i + 1 - k]:
                        array[i - k], array[i + 1 - k] = array[i + 1 - k], array[i - k]
                    else:
                        glue -= 1
                sorted = False
                j = i + 1
            # elif not sorted:
            #     s += 1
        n = n + glue
        count += 1
    return count, count_in


size = 10

array = [random.randint(-100, 100) for _ in range(size)]
print(array)
num = buble_sort_desc(array)
print(array)
print(f'Было проведено внешних циклов: {num[0]} и внутренних циклов: {num[1]}')
print()

array = [random.randint(-100, 100) for _ in range(size)]
print(array)
num = buble_sort_desc_new(array)
print(array)
print(f'Было проведено внешних циклов: {num[0]} и внутренних циклов: {num[1]}')
print()

array = [random.randint(-100, 100) for _ in range(size)]
print(array)
num = buble_sort_new(array)
print(array)
print(f'Было проведено внешних циклов: {num[0]} и внутренних циклов: {num[1]}')

"""
Выводы. 
Было реализовано в коде три варианта функции сортировки пузырьковым методом.
Последнюю можно не рассматривать, сделал ее для собственного интереса.
Анализ времени выполнения  функций показал, что усовершенствованная функция buble_sort_new дает статистически 
не значимое улучшение времени выполнения, хоть и экономит в среднем на количестве выполняемых алгоритмом циклов.

Последняя функция, более существенно экономит на количестве циклов, как внешних, так и внутренних, 
но время ее выполнения хуже чем у обычной функции.

Самая "тяжелая" операция - это обмен значениями: array[i], array[i - 1] = array[i -1], array[i]
"""