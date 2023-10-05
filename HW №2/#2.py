numbers = []                                   # создал пустой список
n = int(input("Введите количество целых чисел: "))
for i in range(n):                             # цикл for для получения каждого числа которое ввел
    num = int(input("Введите число: "))        # преобразовал число в целое 
    numbers.append(num)                        # добавил в nummbers с помощью .append(в конец строки)
numbers.sort(reverse=True)                     # sort сортирует cписок numbers в порядке убывания,reserve меняет наоборот порядок элементов(н-р:первый станет последним)
max_number = int(''.join(map(str, numbers)))   # join объединяет в 1 строку,map применяет str к каждому эл-у списка

print(max_number)       