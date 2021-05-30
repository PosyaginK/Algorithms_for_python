# 2. По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.

ax, ay = input('Введите координаты точки 1 (x y): ').split() # Запрашиваем координаты первой точки
bx, by = input('Введите координаты точки 2 (x y): ').split() # Запрашиваем координаты второй точки
ax, ay, bx, by = int(ax), int(ay), int(bx), int(by) # Приводим значения координат к целочисленному типу

print(f'Точка 1:\nкоординаты: x = {ax}, y = {ay}') # Выводим значения координато точек
print(f'Точка 2:\nкоординаты: x = {bx}, y = {by}') #

x = abs(ax - bx) # Вычисляем x, как разность по модулю между координатами по оси x двух точек
y = abs(ay - by) # Вычисляем y, как разность по модулю между координатами по оси y двух точек

k = round(y / x, 2) # Вычисляем k, как отношение y к x
b = round((k * ax) + ay, 2) # Вычисляем b, как сумму координаты y первой точки и произведения координаты x этой же точки на k

print(f'y = {k}x + {b}') # Выводим уравнение