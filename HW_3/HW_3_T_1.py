# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

result = {}
for i in range(2, 10):
    count = 0
    for el in range(2, 100):
        if el % i == 0:
            count += 1
    result[i] = count

print(result)