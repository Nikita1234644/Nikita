X=int(input('X:'))
Y=int(input('Y:'))
for i in range(X, Y):
    if i%5==0:
        print('Числа кратные 5-ти:',i) #Когда пишу sum(i) выдает ошибку,что "Объект Int не является итеративным"
