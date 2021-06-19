# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random

def create_graph(n, per=1.0):
    assert 0 < per <= 1, 'Неверный диапазон'
    graph = {}

    for i in range(n):
        graph[i] = set()
        count_edge = random.randrange(1, int(n * per))
        while len(graph[i]) < count_edge:
            edge = random.randrange(0, n)
            if edge != i:
                graph[i].add(edge)

    return graph

graph = create_graph(20, 0.5)
print('*' * 50, '\n', 'Наш граф')
for i in graph:
    print(f'{i}: {list(graph[i])}')
print('*' * 50)

def dfs(graph, start):
    path = [] # Путь по которому будем двигаться
    parent = [None for _ in range(len(graph))] # Список родителей
    is_visited = [False] * len(graph)

    def _dfs(vertex): # Внутренняя функция, которая обходит граф начиная с вершины vertex
        is_visited[vertex] = True # Отмечаем вершину как посещенную
        path.append(vertex) # Добавляем ее к пути

        for item in graph[vertex]: # Цикл for для просмотра множества вершин,в которые мы можем перейти из данной
            if not is_visited[item]: # Если очередная вершина из множества еще не была посещена, то
                parent[item] = vertex # Указываем родителя для этой вершины (нашу текущую вершину)
                _dfs(item) # Функция вызывает сама себя, передавая как аргумент новую вершину, ту в которую мы перешли
                path.append(vertex) # Дабваляем в список пути вершину vertex

        else:
            path.append(-vertex)

    _dfs(start)

    return parent, path

parent, path = dfs(graph, 0)
print(parent)

for i, vertex in enumerate(path):
    if i % 10 == 0:
        print()

    print(f'{vertex:>8};', end='')