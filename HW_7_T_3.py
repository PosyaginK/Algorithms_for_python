# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

m = 5
size = 2 * m + 1
array = []
for i in range(size):
    array.append(random.randint(0, 100))
print(f'Исходный массив: {array}')

def search_med(array):
    left = []
    mid = []
    right = []

    ind = 0
    while ind < len(array):
        middle = len(array) // 2
        el = array[ind]
        lo = mi = hi = 0
        for j in range(len(array)):
            if j == ind:
                pass
            else:
                if el > array[j]:
                    hi += 1
                elif el < array[j]:
                    lo += 1
                elif el == array[j]:
                    mi += 1
                else:
                    print(':)')

        if lo > middle:
            left.append(el)
        elif hi > middle:
            right.append(el)
        elif hi == lo:
            mid.append(el)
        else:
            mid.append(el)

        ind += 1
    print(f'\n{"*" * 10 * m}\n')
    mediana = mid[0]
    print(f'Меньшие числа массива: {left}\nМедиана: {mediana}\nБольшие числа массива: {right}')

search_med(array)