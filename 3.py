import math

# Количество итераций цикла
print("Сколько повторений нужно совершить циклу?\n")
iterations = int(input())
#Начало цикла вычислений
for i in range(iterations):
    print(" 1 - Функция G, 2 - Функция F, 3 - Функция Y, Введите число: \n")
    number = int(input())
    if number == 1:
        # Вывод G 
        a = float(input("Введите число a: "))
        border1 = int(input("\nВведите минимальное значение для х: "))
        border2 = int(input("\nВведите максимальное значение для х: "))
        x = float(input("\nВведите число x: "))
        if x < border1 or x > border2:
            print("\n Такой x не помещается в заданные границы")
            continue
        if a == 0 and x == 0:
            print("\nПолучается деление на ноль.")
        else:
            G = 0 - (3*(14*a**2 + 23*a*x - 30*x**2)) / ((0-(9*a**2)) + 37*a*x + 40*x**2)
            print("\nG = ", G)
        # Возможность остановки вычислений
            answer = str(input("\nВы хотите остановить вычисления?\n"))
            if answer == 'да' or answer == 'yes':
                print("\nКонец вычислений")
                break

    elif number == 2:
        # Вывод F
        a = float(input("Введите число a: "))
        border1 = int(input("\nВведите минимальное значение для х: "))
        border2 = int(input("\nВведите максимальное значение для х: "))
        x = float(input("\nВведите число x: "))
        if x < border1 or x > border2:
            print("\n Такой x не помещается в заданные границы")
            continue
        if (a >= -4 and a <= 4) and (x >= -4 and x <= 4):
            F = math.0 - tan(18*a**2 - a*x - 4*x**2)
            print("\nF = ", F)
            # Возможность остановки вычислений
            answer = str(input("\nВы хотите остановить вычисления?\n"))
            if answer == 'да' or answer == 'yes':
                print("\nКонец вычислений")
                break
        else:
            print("\nЧисло слишком большое!")
            
    elif number == 3:
        # Вывод Y
        a = float(input("Введите число a: "))
        border1 = int(input("\nВведите минимальное значение для х: "))
        border2 = int(input("\nВведите максимальное значение для х: "))
        x = float(input("\nВведите число x: "))
        if x < border1 or x > border2:
            print("\n Такой x не помещается в заданные границы")
            continue
        if a!=0 and x !=0:
            print("\nНевозможно сосчитать функцию. Работает только при a=0 и x=0")
        else:
            Y = math.(log(35*a**2 - 27*a*x + 4*x**2 +1))/log(2)
            print("\nY = ", Y)
            # Возможность остановки вычислений
            answer = str(input("\nВы хотите остановить вычисления?\n"))
            if answer == 'да' or answer == 'yes':
                print("\nКонец вычислений")
                break
            
    else:
        # Ошибочная ветвь
        print("Таких функций нет. Ошибка.")
print("\nКонец программы")
