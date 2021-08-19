# 4. Определить, какое число в массиве встречается чаще всего.

import random

m_lst = []

for i in range(0, 20):
    a = random.randint(1, 10)
    m_lst.append(a)

print(m_lst)

max_count = 1
max_el = 1

for i in m_lst:
    count = 0
    for j in m_lst:
        if i == j:
            count += 1
    if count > max_count:
        max_count = count
        max_el = i

print(f'Больше всего в массиве встречается число: {max_el}. Ровно {max_count} раз!')