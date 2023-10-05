elements = []                                # создал пустой список "elements"
while True:                                  # запустил бесконечный цикл       
    user_input = input("Введите элемент: ")  # вводим элемент вручную
    if user_input == "":                     # проверяем пустая ли строка 
        break                                # да - прерываем цикл с помощью break
    elements.append(user_input)              # нет - значение добавляется в конец списка
print("Итоговый список:", elements)           