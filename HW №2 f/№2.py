x= []                                  
y = input("Введите количество целых чисел: ")
while y:    
    x.append(y)
    y = input("Введите число: ")                       
x.sort(reverse=True)               
print("".join(x))   
