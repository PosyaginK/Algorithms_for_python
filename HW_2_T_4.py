# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элмементов ряда (1, -0.5, 0.25, -0.125,… ): '))
n_copy = n # (Для вывода)

el = 1
summ = 0
while n > 0:
    summ += el
    el /= -2
    n -= 1

print(f'Сумма {n_copy} элементов ряда (1, -0.5, 0.25, -0.125,… ) равна {summ}')

