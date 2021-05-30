# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

m_lst = []

for i in range(0, 15):
    x = random.randint(0, 100)
    a = random.randint(1, 100)
    if x % 2 == 0:
        a = a * (-1)
    m_lst.append(a)

print(f'Массив: {m_lst}')

max_negative_el = 100

for el in m_lst:
    if el < 0:
        el = el * (-1)
        if el < max_negative_el:
            max_negative_el = el

print(f'Максимальный отрицательный элемент массива: {max_negative_el * (-1)}')