# палиндром ли это
str = input('Введите строку для проверки:')
if str==str[::-1]:
    print('Палиндром')
else:
    print('Это не палиндром')
