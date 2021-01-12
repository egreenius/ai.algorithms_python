"""
 Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено
 число 3486, надо вывести 6843.
"""


def reverse(num):
    rev_num = ''
    while num != 0:
        rev_num += f'{num % 10}'
        num //= 10
    return rev_num


n = int(input('Введите целое число: '))
print('Вы ввели: ', n)
print('Обратное число: ', reverse(n))

# Вариант 1
num = int(input('Введите целое  число'))
res = 0
while num > 0:
    res = res * 10 + num % 10
    num //= 10
print(res)

# Вариант 2
num = input('Введите целое число')
res = ''
for i in num:
    res = i + res
print(res)

# Вариант 3 !
num = input('Введите целое число')
res = num[::-1]
print(res)
