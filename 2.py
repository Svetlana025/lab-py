import math

print(" 1 - Функция G, 2 - Функция F, 3 - Функция Y, Введите число: \n")
number = int(input())
if number == 1:
    # Вывод G 
    a = float(input("Введите число a: "))
    x = float(input("\nВведите число x: "))
    if a == 0 and x == 0:
        print("\nПолучается деление на ноль.")
    else:
        G = -(3*(14*(a*2)+23*a*x-30*(x*2)))/-9*(a*2)+37*a*x+40*(x*2)
        print("\nG = ", G)
elif number == 2:
    # Вывод F
    a = float(input("Введите число a: "))
    x = float(input("\nВведите число x: "))
    if (a >= -4 and a <= 4) and (x >= -4 and x <= 4):
        F = -tan(18*(a*2)-a*x-4*(x*2))
        print("\nF = ", F)
    else:
        print("\nЧисло слишком большое!")
elif number == 3:
    # Вывод Y
    a = float(input("Введите число a: "))
    x = float(input("\nВведите число x: "))
    if a!=0 and x !=0:
        print("\nНевозможно сосчитать функцию. Работает только при a=0 и x=0")
    else:
        Y = log(35*(a*2)-27*a*x+4*(x*2)+1)/log(2)
        print("\nY = ", Y)
else:
    # Ошибочная ветвь
    print("Таких функций нет. Ошибка.")
