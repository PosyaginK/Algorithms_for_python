# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random

size = 10

array = []
for i in range(size):
    array.append(random.randint(-100, 100))

print(f'Исходный массив: {array}')

def sort_array(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

sort_array(array)
print(f'Отсортированный массив: {array}')

print('*' * 100)
# Второй вартант реализации:
array = []
for i in range(size):
    array.append(random.randint(-100, 100))

print(f'Исходный массив: {array}')
def sort_array2(array):
    for i in range(size):
        for j in range(0, size - i - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
sort_array2(array)
print(f'Отсортированный массив: {array}')