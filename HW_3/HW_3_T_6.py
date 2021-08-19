# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

m_lst = []

for i in range(0, 15):
    a = random.randint(1, 100)
    m_lst.append(a)

print(f'Массив: {m_lst}')

max_el = 0
max_el_indx = 0
min_el = 100
min_el_indx = 0

for el in m_lst:
    if el > max_el:
        max_el = el
        max_el_indx = m_lst.index(el)
    elif el < min_el:
        min_el = el
        min_el_indx = m_lst.index(el)

print(f'Максимальный элемент массива: {max_el} (индекс {max_el_indx})\nМинимальный элемент массива: {min_el} (индекс {min_el_indx})')

summ = 0

for el in m_lst:
    if (m_lst.index(el) > min_el_indx and m_lst.index(el) < max_el_indx) or\
            (m_lst.index(el) < min_el_indx and m_lst.index(el) > max_el_indx):
        summ += el

print(f'Сумма элементов между минимальным и максимальным элементами массива равна {summ}')