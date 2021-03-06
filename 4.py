import math

#Шаблон
shablon = float(input("Напишите значение, которое нужно найти в результатах "))
shab_counter = 0
# Количество итераций цикла
iterations = input("Сколько повторений нужно совершить циклу? ")
iterations = int(iterations)
# Массивы для записи введенных данных
array_a = []
array_x = []
# Переменные для записи максимальных и минимальных значений
min_a = 0
min_x = 0
max_a = 0
max_x = 0
#Начало цикла вычислений
for i in range(iterations):
    print("1 - Функция G, 2 - Функция F, 3 - Функция Y, Введите число: ")
    number = input()
    number = int(number)
    if number == 1:
        # Вывод G
        bordera1 = int(input("Введите минимальное значение для a: "))
        bordera2 = int(input("Введите максимальное значение для a: "))
        a = input("Введите число a: ")
        a = float(a)
        array_a.append(a)
        if a < bordera1 or a > bordera2:
            print("Такой a не помещается в заданные границы")
            continue
        borderx1 = int(input("Введите минимальное значение для х: "))
        borderx2 = int(input("Введите максимальное значение для х: "))
        x = input("Введите число x: ")
        x = float(x)
        array_x.append(x)
        if x < borderx1 or x > borderx2:
            print("Такой x не помещается в заданные границы")
            continue
        if a == 0 and x == 0:
            print("Получается деление на ноль.")
        else:
            G = -(3*(14*(a*2)+23*a*x-30*(x*2)))/-9*(a*2)+37*a*x+40*(x*2)
            print("G = ", G)
        # Возможность остановки вычислений
            answer = str(input("Вы хотите остановить вычисления?\n"))
            if answer == 'да' or answer == 'yes':
                print("Конец вычислений")
                break

    elif number == 2:
        # Вывод F
        bordera1 = int(input("Введите минимальное значение для a: "))
        bordera2 = int(input("Введите максимальное значение для a: "))
        a = input("Введите число a: ")
        a = float(a)
        array_a.append(a)
        if a < bordera1 or a > bordera2:
            print("Такой a не помещается в заданные границы")
            continue
        a = float(input("Введите число a: "))
        borderx1 = int(input("Введите минимальное значение для х: "))
        borderx2 = int(input("Введите максимальное значение для х: "))
        x = input("Введите число x: ")
        x = float(x)
        array_x.append(x)
        if x < borderx1 or x > borderx2:
            print("Такой x не помещается в заданные границы")
            continue
        if (a >= -4 and a <= 4) and (x >= -4 and x <= 4):
            F = math.-tan(18*(a*2)-a*x-4*(x*2))
            print("F = ", F)
            # Возможность остановки вычислений
            answer = str(input("Вы хотите остановить вычисления?\n"))
            if answer == 'да' or answer == 'yes':
                print("Конец вычислений")
                break
        else:
            print("Число слишком большое!")
            
    elif number == 3:
        # Вывод Y
        bordera1 = int(input("Введите минимальное значение для a: "))
        bordera2 = int(input("Введите максимальное значение для a: "))
        a = input("Введите число a: ")
        a = float(a)
        array_a.append(a)
        if a < bordera1 or a > bordera2:
            print("Такой a не помещается в заданные границы")
            continue
        a = float(input("Введите число a: "))
        borderx1 = int(input("Введите минимальное значение для х: "))
        borderx2 = int(input("Введите максимальное значение для х: "))
        x = input("Введите число x: ")
        x = float(x)
        array_x.append(x)
        if x < borderx1 or x > borderx2:
            print("Такой x не помещается в заданные границы")
            continue
        if a!=0 and x !=0:
            print("Невозможно сосчитать функцию. Работает только при a=0 и x=0")
        else:
            Y = math.log(35*(a*2)-27*a*x+4*(x*2)+1)/math.log(2)
            print("Y = ", Y)
            # Возможность остановки вычислений
            answer = str(input("\nВы хотите остановить вычисления?\n"))
            if answer == 'да' or answer == 'yes':
                print("\nКонец вычислений")
                break
            
    else:
        # Ошибочная ветвь
        print("Таких функций нет. Ошибка.")
print("Полученные значения ", end = "")
for k in range(iterations):
    print("a[",k,"] is: ", array_a[k]," ",sep ="", end = "")
    if array_a[k] == shablon:
        print(array_a[k]," - шаблонное значение", sep = "", end = "")
        shab_counter += 1
    print("x[",k,"] is: ", array_x[k], " ", sep = "", end = "")
    if array_x[k] == shablon:
        print(array_x[k]," - шаблонное значение", sep = "", end = "")
        shab_counter += 1
for j in range(iterations):
    if array_a[j] > max_a:
        max_a = array_a[j]
    if array_a[j] < min_a:
        min_a = array_a[j]
    if array_x[j] > max_x:
        max_x = array_x[j]
    if array_x[j] < min_x:
        min_x = array_x[j]
print("\nМинимальный а: ", min_a, "Максимальный а: ", max_a, "\nМинимальный х: ", min_x, "Максимальный х: ", max_x)
print("Количество шаблонных значений: ",shab_counter)
print("Конец программы")
