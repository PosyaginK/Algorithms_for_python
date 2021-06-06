# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его
# улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».

# Первый вариант (Решето Эратосфена):
def erat(pos):
    result = []
    l = pos
    while len(result) != pos:
        l += 1
        s_list = [i for i in range(l)]
        s_list[1] = 0
        for i in range(2, l):
            if s_list[i] != 0:
                j = i * 2
                while j < l:
                    s_list[j] = 0
                    j += i
        result = [i for i in s_list if i != 0]
    return result[-1]

print(erat(30))
# erat(40)

# Второй вариант:

def erat(pos):
    result = [2]
    next_el = 2
    while len(result) != pos:
        next_el += 1
        check = 0
        for el in result:
            if next_el % el == 0:
                check += 1
        if check == 0:
            result.append(next_el)

    return result[-1]

print(erat(30))


