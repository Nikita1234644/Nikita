numbers = []                                  
n = int(input("Введите количество целых чисел: "))
for i in range(n):                             # цикл for для получения каждого числа которое ввел
    num = int(input("Введите число: "))        
    numbers.append(num)                        # добавил в numbers с помощью .append(в конец строки)
numbers.sort(reverse=True)                     # sort сортирует cписок в порядке убывания,reserve меняет наоборот порядок эл-ов(н-р:первый станет последним)
max_numb = int(''.join(map(str, numbers)))     # .join объединяет в 1 строку,map применяет str к каждому эл-у списка
print(max_numb)       