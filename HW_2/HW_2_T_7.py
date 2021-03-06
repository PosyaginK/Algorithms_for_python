# 7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.

n = int(input('Введите n: '))

l_side = 0
el = 1
while el <= n:
    l_side += el
    el += 1

r_side = int((n * (n + 1)) / 2)

if l_side == r_side:
    print(f'1 + 2 + ... + {n} = {n}({n} + 1) / 2 = {l_side}')
    print('Доказано!')
else:
    print(f'1 + 2 + ... + {n} != {n}({n} + 1) / 2')
    print(f'1 + 2 + ... + {n} = {l_side}')
    print(f'{n}({n} + 1) / 2 = {r_side}')



