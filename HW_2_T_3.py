# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

num = int(input('Введите число: '))
num_copy = num # (Для вывода)
rev_num = ''

while num / 10 > 0:
    el = str(num % 10)
    num = num // 10
    rev_num = rev_num + el

rev_num = int(rev_num)
print(f'{num_copy} наоборот - {rev_num}')