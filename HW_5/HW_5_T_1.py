# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.
from collections import namedtuple

N = int(input('Количество предприятий: '))
orgs = []
parametrs = ['name', 'kvart_1', 'kvart_2', 'kvart_3', 'kvart_4']
Company = namedtuple('Company', parametrs)

for i in range(N):
    org = Company(str(input('Имя: ')), int(input('Первый квартал: ')), int(input('Второй квартал: ')),\
                  int(input('Третий квартал: ')), int(input('Четвертый квартал: ')))
    orgs.append(org)

mid_p = 0
for i in orgs:
    mid = i.kvart_1 + i.kvart_2 + i.kvart_3 + i.kvart_4
    mid_p += mid
mid_p /= N

h = []
l = []
for i in orgs:
    mid = i.kvart_1 + i.kvart_2 + i.kvart_3 + i.kvart_4
    if mid > mid_p:
        h.append(i.name)
    elif mid < mid_p:
        l.append(i.name)

print(f'Средняя прибыль {N} компаний за год: {mid_p}')
print(f'Предприятия с прибылью выше среднего: {", ".join(h)}')
print(f'Предприятия с прибылью ниже среднего: {", ".join(l)}')