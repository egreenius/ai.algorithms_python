"""
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых
трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
 число 3486, надо вывести 6843.
"""


import cProfile


def test_reverse(num, mun):
    num = str(num)
    spam = num[::-1]
    assert spam == mun
    return True


# Вариант 1
def reverse(num):
    rev_num = ''
    while num != 0:
        rev_num += f'{num % 10}'
        num //= 10
    return rev_num

# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse(12345)"
# 1000 loops, best of 5: 1.16 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse(1234512345)"
# 1000 loops, best of 5: 2.35 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse(123451234512345)"
# 1000 loops, best of 5: 3.8 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse(12345123451234512345)"
# 1000 loops, best of 5: 5.26 usec per loop
# При увеличении длины входных данных в два раза, время также увеличивается в два раза. Сложность алгоритма примерно O(n)

# cProfile.run('reverse(12345123451234512345)')
#       1    0.000    0.000    0.000    0.000 les_4_hw_1.py:29(reverse)
# Результаты для разной длины входных данных выглядят одинаково. Никаких особенностей не отмечено.


# Вариант 2
def reverse_1(num):
    res = 0
    while num > 0:
        res = res * 10 + num % 10
        num //= 10
    return str(res)
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_1(12345)"
# 1000 loops, best of 5: 1.04 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_1(1234512345)"
# 1000 loops, best of 5: 1.81 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_1(123451234512345)"
# 1000 loops, best of 5: 2.94 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_1(12345123451234512345)"
# 1000 loops, best of 5: 4.16 usec per loop
# При увеличении длины входных данных в два раза, время также увеличивается в два раза. Сложность алгоритма примерно O(n)

# cProfile.run('reverse_1(1234512345123451234512345123451234512345)')
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_hw_1.py:50(reverse_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Результаты для разной длины входных данных выглядят одинаково. Никаких особенностей не отмечено.


# Вариант 3
def reverse_2(num):
    num = str(num)
    res = num[::-1]
    return res
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_2(12345)"
# 1000 loops, best of 5: 409 nsec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_2(1234512345)"
# 1000 loops, best of 5: 435 nsec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_2(123451234512345)"
# 1000 loops, best of 5: 454 nsec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_2(12345123451234512345)"
# 1000 loops, best of 5: 488 nsec per loop
# При увеличении длины входных данных, рост времени исполнения не значительный. Сложность алгоритма O(1)?

# cProfile.run('reverse_1(1234512345123451234512345123451234512345)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_hw_1.py:77(reverse_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Результаты для разной длины входных данных выглядят одинаково. Никаких особенностей не отмечено.


# Вариант 4
def reverse_3(num):
    res = ''
    for i in str(num):
        res = i + res
    return res
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_3(12345)"
# 1000 loops, best of 5: 727 nsec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_3(1234512345)"
# 1000 loops, best of 5: 1.04 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_3(123451234512345)"
# 1000 loops, best of 5: 1.39 usec per loop
# python3 -m timeit -n 1000 -s "import les_4_hw_1" "les_4_hw_1.reverse_3(12345123451234512345)"
# 1000 loops, best of 5: 1.75 usec per loop
# При увеличении длины входных данных в два раза, время также увеличивается, но не значительно.
# Сложность алгоритма примерно O(n) -?

# cProfile.run('reverse_3(1234512345123451234512345123451234512345)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_hw_1.py:101(reverse_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# Результаты для разной длины входных данных выглядят одинаково. Никаких особенностей не отмечено.


# Выводы. Наиболее эффективный алгоритм reverse_2, со срезом. Время выполнения практически не зависит
# от длины входных данных. Второй по эффективности алгоритм revers_3. cProfile никакой дополнительной информации не дал,
# так как все алгоритмы достаточно простые.

# n = 123456789
# test_reverse(n, reverse(n))
# print('1-Ok')
# test_reverse(n, reverse_1(n))
# print('2-Ok')
# test_reverse(n, reverse_2(n))
# print('3-Ok')
# test_reverse(n, reverse_3(n))
# print('4-Ok')