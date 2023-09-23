# Определить в какой четверти находится точка 
y=float(input('x:'))
x=float(input('y:'))
if y==0:
    print('Точка на оси ординат')
elif x==0:
    print('Точка на оси абсцисс')
elif y>0 and x>0:
    print('Точка в 1-ой четверти')
elif y>0 and x<0:
    print('Точка во 2-ой четверти')
elif y<0 and x<0:
    print('Точка в 3-ей четверти')
elif y<0 and x>0:
    print('Точка в 4-ой четверти')
else:
    print('Точка в начале координат')
    
