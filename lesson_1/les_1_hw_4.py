'''
Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
'''

# пользователь вводит буквы
a = input('Введите 1-ую букву от a до z: ')
b = input('Введите 2-ую букву от a до z: ')

# находим позиции введенных букв в алфавите, вычитая код буквы - a, и добавляя 1.
a = ord(a) - ord('a') + 1
b = ord(b) - ord('a') + 1

# находим количество букв между введенными буквами, разница позиций по модулю - 1.
c = abs(a - b) - 1

print('Позиция 1-й буквы: ', a)
print('Позиция 2-й буквы: ', b)
print('Количество букв в алфавите между введенными буквами: ', c)
