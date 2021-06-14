# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления, задача решается в
# несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит. Поэтому использование встроенных
# функций для перевода из одной системы счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque

n1 = str(input('Первое шестнадцатеричное число: ')) # Первое число
n2 = str(input('Второе шестнадцатеричное число: ')) # Второе число
print(f'{n1} + {n2} = ', end='')
hex_list = deque('0123456789abcdef') # Очередь символов шестрандцатеричной системы

hex_dict = {} # Словарь шестнадцатеричной системы
for i in range(16): # Формируем словарь для перевода из десятичной системы в шестнадцатеричную и обратно
    hex_el = hex_list.popleft()
    l = {hex_el: i}
    m = {i: hex_el}
    hex_dict.update(l)
    hex_dict.update(m)

if len(n2) > len(n1): # Создаем очередь из элементов шестнадцатеричного числа (Первое - то, кторое длинее)
    n1, n2 = deque(n2[::-1]), deque(n1[::-1])
else:
    n1, n2 = deque(n1[::-1]), deque(n2[::-1])

result = [] # Будующий результат сложения
j = 0 # Счетчик индексов меньшего числа
ed = 0 # Это для переноса единицы в следующий разряд, в случае если сумма элементов больше 16
for i in n1: # Идем по большему числу
    first = hex_dict.get(i)
    if j < len(n2): # Если меньшее число еще не закончилось, то:
        second = hex_dict.get(n2[j]) # Берем элемент этого числа,
        r = first + second + ed # И скаладываем с элементом первого числа и мнимой единицей.
        if first + second > 15:
            ed = 1
            r -= 16
        else:
            ed = 0
        result.append(r) # Добавляем полученную сумму в наш результат
    else:
        result.append(first + ed) # Иначе просто добавляем в результат элемент из первого числа.
        if first + ed > 15:
            ed = 1
        else:
            ed = 0
    j += 1 # Прибавляем счетчик

result = result[::-1]
hex_resalt = ''
for el in result:
    hex_el = hex_dict.get(el)
    hex_resalt += hex_el

print(hex_resalt)