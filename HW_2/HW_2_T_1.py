# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся
# пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
# неверный знак (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
while True:
    op = str(input('Введите операцию (+, -, *, /). Для выхода введите 0: '))
    if op == '0':
        print('Программа завершена')
        break

    n1 = int(input('Введите первое число: '))
    n2 = int(input('Введите второе число: '))

    if n2 == 0 and op == '/':
        print('На ноль делить нельзя!')
    else:
        if op == '+':
            print(f'{n1} + {n2} = {n1 + n2}')
        elif op == '-':
            print(f'{n1} - {n2} = {n1 - n2}')
        elif op == '*':
            print(f'{n1} * {n2} = {n1 * n2}')
        elif op == '/':
            print(f'{n1} / {n2} = {n1 / n2}')
        else:
            print('Неизвестная операция.')
    print('-' * 100)