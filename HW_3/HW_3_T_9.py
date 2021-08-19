# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

row = 5
colum = 5
mtrx = [[random.randint(0, 100) for _ in range(colum)] for _ in range(row)]

for row in mtrx:
    for el in row:
        print(f'{el:>4}', end='')
    print()

min_els = [101 for _ in range(colum)]

for row in mtrx:
    for i in range(len(row)):
        if row[i] < min_els[i]:
            min_els.insert(i, row[i])
            min_els.pop(i + 1)
print(f'Минимальные элементы столбцов матрицы: {min_els}')

max_min_el = 0

for el in min_els:
    if el > max_min_el:
        max_min_el = el

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы: {max_min_el}')