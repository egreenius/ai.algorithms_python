"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры. """

n = int(input('Сколько чисел Вы хотите ввести? '))
d = int(input('Какую цифру нужно посчитать? '))
count = 0
for i in range(1, n + 1):
    un = int(input(f'{i} - е число: '))  #  можно запоминать строку и искать строка.count(digit)
    while un != 0:
        if un % 10 == d:
            count += 1
        un = un // 10

print(f'Вы ввели чисел - {n}, в которых цифра {d} встречается {count} раз(а)')