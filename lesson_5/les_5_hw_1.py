"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import defaultdict


n = int(input('Введите количество предприятий: '))
data = defaultdict(float)  # информация о прибыли по предприятиям
average_p = 0  # средняя прибыль
for i in range(1, n + 1):
    print()
    name = input(f'Введите наименование  {i} ой компании: ')
    for j in range(1, 5):
        profit = float(input(f'Введите прибыль {i} ой компании за {j}-й квартал: '))
        data[name] += profit  # накапливаем значения прибыли предприятия за год, используя defaultdict
    average_p += data[name]

average_p = average_p/n

print()
for name, profit in data.items():  # распечатываем результат
    if profit > average_p:
        print(f'Прибыль предприятия {name} выше среднего {average_p} и составляет {profit}')
    elif profit < average_p:
        print(f'Прибыль предприятия {name} ниже среднего {average_p} и составляет {profit}')

"""
Другой вариант:
from collections import namedtuple
n = int(input('Введите количество предприятий: '))

prop = ['q1', 'q2', 'q3', 'q4']
NewCompany = namedtuple('NewCompany', prop)
all_companies = {}
total = 0

for i in range(n):
    company = input('Укажите название предприятия: ')
    q = []
    for j in range(1,5):
        profit = int(input(f'Укажите прибыль за {j} квартал: '))
        q.append(profit)
    all_companies[company] = NewCompany(*q)
    total += sum(q)

print(f'Вы ввели следующие данные:\n'
      f'{all_companies}\n'
      f'Средняя прибыль по предприятиям: {total/n}\n')

for name, profit in all_companies.items():
    print(f'Прибыль компании "{name}" за год составила: {sum(profit)}')
    if sum(profit) < total/n:
        print(f'"{name}" имеет прибыль ниже среднего\n')
    else:
        print(f'"{name}" имеет прибыль выше среднего\n')
"""
