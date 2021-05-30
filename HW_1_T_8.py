# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

n_1 = int(input('Введите первое число: ')) # Запрашиваем первое число
n_2 = int(input('Введите второе число: ')) # Запрашиваем второе число
n_3 = int(input('Введите третье число: ')) # Запрашиваем третье число

if n_1 == n_2 and n_1 == n_3: # Если все три числа равны, то
    print('Невозможно опредеить среднее число, так как все числа равны :(') # Мы не можем определить среднее
elif n_1 == n_2 or n_1 == n_3 or n_2 == n_3: # Даже если хотябы два числа из трех равны -
    print('Невозможно определить среднее число, так как два из трех числе равны :(') # Мы не можем определить среднее
else: # Если же все числа разные, то
    if n_1 != max(n_1, n_2, n_3) and n_1 != min(n_1, n_2, n_3): # Если число 1 не является максимальным  и минимальным, то
        print(f'Среднее число - {n_1}') # число 1 - среднее
    elif n_2 != max(n_1, n_2, n_3) and n_2 != min(n_1, n_2, n_3): # Иначе если число 2 не является максимальным и минимальным, то
        print(f'Среднее число - {n_2}') # число 2 - среднее
    elif n_3 != max(n_1, n_2, n_3) and n_3 != min(n_1, n_2, n_3): # Если число 3 не является максимальным  и минимальным, то
        print(f'Среднее число - {n_2}') # число 3 - средее