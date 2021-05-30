# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
count = int(input('Сколько чисел вы хотите ввести: '))

max_summ = 0
max_num = 0

i = 1
while i <= count:
    num = int(input(f'{i}: Введите натуральное число: '))
    num_cp = num

    summ = 0
    while num / 10 > 0:
        el = num % 10
        summ += el
        num //= 10

    if summ > max_summ:
        max_summ = summ
        max_num = num_cp
    i += 1

print(f'Наибольшее по сумме цифр число: {max_num}, сумма цифр = {max_summ}')