# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба минимальны), так и различаться.

import random

m_lst = []

for i in range(0, 15):
    a = random.randint(1, 100)
    m_lst.append(a)

print(f'Массив: {m_lst}')

min_el1 = m_lst[0]
min_el2 = m_lst[0]

for el in m_lst:
    if el < min_el1:
        min_el1 = el
m_lst.remove(min_el1)
for el in m_lst:
    if el < min_el2:
        min_el2 = el

print(f'Минимальные элементы массива: {min_el1} и {min_el2}')