"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
которые необходимо обойти.
"""
from collections import deque


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length  # в списке будем хранить информацию, посещали мы вершину или нет
    cost = [float('inf')] * length  # в этом списке стоимость пути, пока лежит бесконечность
    parent = [-1] * length  # пока не знаем родителя вершины то -1, а когда узнаем будем записывать родителя - номер вершины

    cost[start] = 0  # стоимость до вершины с которой начинаем = 0
    min_cost = 0  # здесь будем хранить минимальную стоимость. Будет показывать двигаемся мы по графу или уже нет
    start_way = start  # сохраним начальное значение вершины, с которой начинаем обход

    while min_cost < float('inf'):  # базовый цикл алгоритма Дейкстры

        is_visited[start] = True  # стартовая вершина явл. посещенной

        for i, vertex in enumerate(graph[start]):  # пройдемся матрице смежности вершины, с которой начали
            if vertex != 0 and not is_visited[i]:  # на мой взгляд имена переменных не соответствуют факту,
                # но менять не стал

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start  # запишем родителей, для каждой рассмотренной вершины. Значения могут меняться
                    # по ходу движения по общему циклу

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i  # здесь вся магия. перемещаем начало обхода на новую вершину

    """ Здесь начинается доработка по заданию. Используем список parent, в нем есть вся нужная нам информация"""
    way = [None] * length # здесь будем хранить путь к вершинам
    way_cost = {}  # в словаре будем хранить вершину и соответствующие ей путь и стоимость
    for i in range(length):  # цикл обхода по списку parent
        way[i] = deque()
        if cost[i] == float('inf'):
            way[i].appendleft('Нет маршрута')
        else:
            way[i].appendleft(i)
        if parent[i] == -1:
            way_cost[i] = way[i], cost[i]
            continue
        j = i
        while parent[j] != start_way:
            way[i].appendleft(parent[j])
            j = parent[j]
        else:
            way[i].appendleft(start_way)
        way_cost[i] = way[i], cost[i]
    return way_cost


s = int(input('От какой вершины идти: '))
way_cost = dijkstra(g, s)
print(f'Точка старта {s}')
print('Длина пути и маршрут до вершин:')
for key, value in way_cost.items():
    print(f'{key}: длина пути: {value[1]},\t маршрут: {list(value[0])}')
