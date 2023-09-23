# «Делить на ноль нельзя!».
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
d = float(input('d='))
f = float(input('f='))
if f-d != 0:
    rep = (a*b-c) / (f-d)
    print(rep)
else:
    print("Делить на ноль нельзя!")
