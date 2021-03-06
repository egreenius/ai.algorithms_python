"""
2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
"""

import cProfile, math


def test_prime_n(k, n=10000):  # функция проверки алгоритма нахождения простого числа по его индексу. k - позиция
    # числа в списке простых чисел. к - начинается с 1.  При n = 10 000, количество простых чисед - 1229
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):  # вычисляем простые числа с помощью алгоритма решето Эратосфена
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]

    assert len(res) > k > 0  # проверяем, что запрашиваемый индекс простого числа входит в диапазон тестирования
    return res[k - 1]


def sieve_i(n):
    if n == 1:
        return 2
    pos = 1  # переменная для хранения позиции простого числа в последовательности простых чисел
    first = 3  # первое число диапазона, в которой будем искать простые числа
    last = n * 4  # определяем последнее число диапазона чисел, где будем искать простые числа
    sieve = [i for i in range(first, last) if i % 2 != 0]  # заполняем решето списком натуральных чисел,
    # исключая кратные 2
    res = [2]  # инициализируем список для хранения простых чисел начальным значением = 2.
    while pos < n:  # внешний цикл работает пока не достигнем результата, то есть pos = n
        for i in range(len(sieve)):  # прокалываем дырки нулями в искомом диапазоне чисел
            if sieve[i] != 0:
                pos += 1  # переменная хранит позицию последнего найденного простого числа
                if pos == n:
                    return sieve[i]  # искомая позиция найдена, возращаем результат
                j = i + sieve[i]  # намечаем дырки для прокалывания
                while j < len(sieve):
                    sieve[j] = 0  # прокалываем
                    j += sieve[i]  # намечаем следующую дырку

        res.extend([i for i in sieve if i != 0])  # добавим просеянный список простых чисел в уже имеющийся список
        # простых чисел

        first, last = last, last + 2 * n  # определяем следующий диапазон чисел для просеивания
        sieve = [i for i in range(first, last) if i % 2 != 0]  # заполняем новый диапазон чисел для просеивания

        for i in range(len(sieve)):  # зачеркиваем нулями не простые числа
            # и возвращаем просеянный список в овновной цикл
            for num in res:
                if sieve[i] % num == 0:  # проверяем числа нового диапазона на делимость на каждое уже определенное
                    # нами простое число в предыдущих диапазонах
                    sieve[i] = 0
                    break  # если нашли хоть одно простое число на которое можно разделить данное, проверять остальные
                    # нет смысла

# Проверяем сложность. Время исполнения:
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.sieve_i(10)"
# 100 loops, best of 5: 6.44 usec per loop
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.sieve_i(100)"
# 100 loops, best of 5: 269 usec per loop
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.sieve_i(500)"
# 100 loops, best of 5: 7.22 msec per loop
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.sieve_i(1000)"
# 100 loops, best of 5: 23.3 msec per loop
# Увеличение длины входных данных в 10 раз увеличивает время примерно в 100 раз. Сложность ориентировочно O(n**2)

# cProfile.run('sieve_i(10)')
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:27(sieve_i)
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:33(<listcomp>)
# cProfile.run('sieve_i(100)')
#         1    0.000    0.000    0.001    0.001 les_4_hw_2.py:27(sieve_i)
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:33(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:47(<listcomp>)
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:51(<listcomp>)
# cProfile.run('sieve_i(1000)')
#         1    0.051    0.051    0.053    0.053 les_4_hw_2.py:27(sieve_i)
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:33(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_hw_2.py:47(<listcomp>)
#         2    0.000    0.000    0.000    0.000 les_4_hw_2.py:51(<listcomp>)
# Для больших значений диапазон дважды расширялся. Время исполнения постепенно увеличивается, рекурсивных вызовов нет


def prime_i(n):  # функция поиска простых чисел перебором проверкой деления на известные простые числа
    pos = 1  # переменная для хранения последней позиции простого числа в последовательности.
    # В позиции 1 находится число 2
    num = 1  # переменная для хранения очередного проверямого числа из последовательности натуральных чисел
    res = [2]  # инициализируем список для хранения простых чисел начальным значением = 2.
    if n == 1:
        return 2
    while pos < n:
        num += 2  # очередное проверяемое число последовательности. Кратные 2 таким образом просеяли.
        for k in res:
            if num % k == 0:
                break
        else:
            pos += 1
            res.append(num)
    return num


# Проверяем сложность. Время исполнения:
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.prime_i(10)"
# 100 loops, best of 5: 4.83 usec per loop
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.prime_i(100)"
# 100 loops, best of 5: 282 usec per loop
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.prime_i(500)"
# 100 loops, best of 5: 6.28 msec per loop
# python3 -m timeit -n 100 -s "import les_4_hw_2" "les_4_hw_2.prime_i(1000)"
# 100 loops, best of 5: 25.5 msec per loop
# Увеличение длины входных данных в 10 раз увеличивает время примерно в 100 раз. Сложность ориентировочно O(n**2)

# cProfile.run('prime_i(10)')
#         1    0.000    0.000    0.000    0.000 les_4_hw_2.py:87(prime_i)
# cProfile.run('prime_i(100)')
#         1    0.001    0.001    0.001    0.001 les_4_hw_2.py:87(prime_i)
# cProfile.run('prime_i(1000)')
#         1    0.052    0.052    0.053    0.053 les_4_hw_2.py:87(prime_i)
# Время исполнения увеличивается. Никаких особенностей не наблюдается.

"""
Вывод:
Время исполнения обоих алгоритмов практически одинаковое. Сложность алгоритмов идентичная

"""


def second(i):
    primes = [2]
    num = 3
    while len(primes) < i:
        flag = True
        for j in primes.copy():
            if num % j == 0:
                flag = False
                break
        if flag:
            primes.append(num)
        num += 1
    return primes[-1]


def first(i):
    primes_qty = 0
    len_array = 2
    while primes_qty <= i:
        primes_qty = len_array / math.log(len_array)
        len_array += 1

    sieve = [_ for _ in range(2, len_array)]

    for num in sieve:
        if sieve.index(num) <= num - 1:
            for j in range(2, len(sieve)):
                if num * j in sieve[num:]:
                    sieve.remove(num * j)
        else:
            break
    return sieve[i - 1]


def solution1(n, pos):
    list_n = [i for i in range(n)]
    list_n[1] = 0
    for x in range(2, n):
        if list_n[x] != 0:
            j = x * 2
            while j < n:
                list_n[j] = 0
                j += x
    results = [i for i in list_n if i != 0]
    return results[pos]


def solution2(n, pos):
    results = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0 and i != j:
                break
        else:
            results.append(i)
    return results[pos]


n = 1200  # натуральное число на входе, представляющее собой индекс (i тое) простое число.
# assert sieve_i(n) == test_prime_n(n)
# assert prime_i(n) == test_prime_n(n)
# assert second(n) == test_prime_n(n)
# assert first(n) == test_prime_n(n)
# assert solution1(n) == test_prime_n(n)
# assert solution2(100000, n) == test_prime_n(n)
print(solution1(10000, 0), test_prime_n(1))
print('Ok')

