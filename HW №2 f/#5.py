x = input("Введите пятизначное число: ")
if len(x) != 5:  # если длина строки не равна 5
    print("Вы ввели не пятизначное число")
else:
    for i in x:  # Запускаем цикл, i хранит значения послед-ти x
        print(i)        