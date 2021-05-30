# 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random

m_lst = []

for i in range(0, 10):
    a = random.randint(1, 100)
    m_lst.append(a)

print(m_lst)

min_el = m_lst[0]
min_ind = 0
max_el = m_lst[-1]
max_ind = 0

for ind in range(0, len(m_lst)):
    if m_lst[ind] > max_el:
        max_el = m_lst[ind]
        max_ind = ind
    elif m_lst[ind] < min_el:
        min_el = m_lst[ind]
        min_ind = ind

print(f'Минимальный элемент -  {min_el}. Он {min_ind + 1} в списке')
print(f'Максимальный элемент -  {max_el}. Он {max_ind + 1} в списке')

m_lst.insert(min_ind, max_el)
m_lst.pop(min_ind + 1)
m_lst.insert(max_ind, min_el)
m_lst.pop(max_ind + 1)

print(m_lst)