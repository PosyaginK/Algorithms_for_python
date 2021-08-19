# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
import random

mtrx = []

for row in range(4):
    print(f'Строка {row + 1}:')
    line = []
    sum = 0
    for colum in range(4):
        el = int(input(f'Элемент {colum + 1}: '))
        line.append(el)
        sum += el
    print(f'Элемент 5: {sum}')
    line.append(sum)
    mtrx.append(line)


for line in mtrx:
    for item in line:
        print(f'{item:>4}', end='')
    print()

