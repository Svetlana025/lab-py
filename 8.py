from math import sqrt
import xlwt
from random import random
from time import time
# Проверка принадлежности 
def point_in_circle(px, py, radius):
    distance = sqrt(px**2 + py**2)
    if distance <= radius:
        print("Точка принадлежит области")
        return 1
    else:
        return 0

# Создание точек
number = int(input("Сколько точек нужно создать? "))
x = []
y = []
for i in range(number):
    x.append(int(random()* number))
    y.append(int(random()* number))
    print("Ваша точка: ", x[i], y[i])
# Построение области
center = int(random()* number)
cx = x[center]
cy = y[center]
print("Центр области: ", cx, cy)
radius = float(input("Каков радиус? "))
# Подсчет времени выполнения
wb = xlwt.Workbook()
file = wb.add_sheet("Результаты")
points_in_circle, total_time = 0, 0
for j in range(number):
    start = time()
    points_in_circle += point_in_circle(x[j],y[j], radius)
    end = time()
    total_time += end - start
    file.write(j, 0, j)
    file.write(j, 1, total_time)
wb.save("Трейд_Питон.xls")
print("Всего точек в области: ", points_in_circle)
