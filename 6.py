import math

#Шаблон
shablon = float(input("Напишите значение, которое нужно найти в результатах "))
shab_counter = 0
# Количество итераций цикла
iterations = int(input("Сколько повторений нужно совершить циклу? "))
# Массивы для записи введенных данных
array_a = []
array_x = []
# Данные
results = []
GFY = {}
res_G = []
res_F = []
res_Y = []

#Начало цикла вычислений
for i in range(iterations):

    # Ввод аргументов функций
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
    # Вывод G
    print("Вычисление фунции G ")
    if a == 0 and x == 0:
        print("При введенных значениях a и x получается деление на ноль.")
        res_G.append("Error")
    else:
        G = -(3*(14*(a*2)+23*a*x-30*(x*2)))/-9*(a*2)+37*a*x+40*(x*2)
        res_G.append(G)
        print("G = ", G)
        # Возможность остановки вычислений
        answer = input("Вы хотите остановить вычисления?\n")
        if answer == 'да' or answer == 'yes':
            print("Конец вычислений")
            break

    # Вывод F
    print("Вычисление функции F ")
    if (a >= -4 and a <= 4) and (x >= -4 and x <= 4):
        F = math.-tan(18*(a*2)-a*x-4*(x*2))
        res_F.append(F)
        print("F = ", F)
        # Возможность остановки вычислений
        answer = input("Вы хотите остановить вычисления?\n")
        if answer == 'да' or answer == 'yes':
            print("Конец вычислений")
            break
    else:
        res_F.append("Error")
        print("При введенных значениях a и x число получается слишком большое!")
            
    # Вывод Y
    print("Вычисление функции Y ")
    if a!=0 and x !=0:
        res_Y.append("Error")
        print("При введенных значениях a и x невозможно сосчитать функцию. Работает только при a=0 и x=0")
    else:
        Y = math.log(35*(a*2)-27*a*x+4*(x*2)+1)/math.log(2)
        res_Y.append(Y)
        print("Y = ", Y)
        # Возможность остановки вычислений
        answer = input("\nВы хотите остановить вычисления?\n")
        if answer == 'да' or answer == 'yes':
            print("\nКонец вычислений")
            break
            
print("Полученные значения ")
min_a,min_x,max_a,max_x = array_a[0], array_x[0], array_a[0], array_x[0]
for k in range(iterations):
    print("\nЦикл вычислений ", k + 1)
    print("a[",k,"] is: ", array_a[k]," ",sep ="", end = "")
    if array_a[k] == shablon:
        print(array_a[k]," - шаблонное значение", sep = "", end = "")
        shab_counter += 1
    print("x[",k,"] is: ", array_x[k], " ", sep = "")
    if array_x[k] == shablon:
        print(array_x[k]," - шаблонное значение", sep = "")
        shab_counter += 1
    if array_a[k] > max_a:
        max_a = array_a[k]
    if array_a[k] < min_a:
        min_a = array_a[k]
    if array_x[k] > max_x:
        max_x = array_x[k]
    if array_x[k] < min_x:
        min_x = array_x[k]
GFY["G"] = res_G
GFY["F"] = res_F
GFY["Y"] = res_Y
results.append(GFY)
print(results)
print("\nМинимальный а: ", min_a, "Максимальный а: ", max_a, "\nМинимальный х: ", min_x, "Максимальный х: ", max_x)
print("Количество шаблонных значений: ",shab_counter)
print("Конец программы")
