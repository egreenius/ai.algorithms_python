"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
считается не решённой.
"""

from hashlib import sha1


def substr_count(s: str, verbose=False) -> int:
    length_s = len(s)
    assert length_s, 'Строка не может быть пустой'

    substr_dict = dict()  # здесь будем накапливать подстроки в качестве ключей и
    # кол-во их вхождений в строку в качестве значений
    # формируем список подстрок перебором, начиная с длины = 1 и до длины всей строки, не включая
    for i in range(length_s):
        for len_subs in range(i + 1, length_s + 1):
            substr = s[i:len_subs]
            if substr != s and substr not in substr_dict:  # добавляем найденные подстроки в словарь в качестве ключей,
                # исключая полную строку
                substr_dict[substr] = 0

    # находим кол-во вхождений подстроки в строку, используя идею Рабина Карпа
    for subs in substr_dict:
        len_sub = len(subs)
        h_subs = sha1(subs.encode('utf-8')).hexdigest()

        for i in range(length_s - len_sub +1):
            if h_subs == sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():
                substr_dict[subs] += 1

    if verbose:  # при желании, печатаем словарь с подстроками и кол-вом вхождений
        print(substr_dict)

    # суммируем количество вхождений каждой подстроки в строке и возвращаем результат
    return sum(i for i in substr_dict.values())


s = input("Введите строку: ")
print(f'Количество подстрок в строке {s} = {substr_count(s)}')
print()
# print(f'Количество подстрок в строке {s} = {substr_count(s, True)}')

