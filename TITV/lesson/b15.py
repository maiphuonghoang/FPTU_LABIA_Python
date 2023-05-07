import math

a = float(input('Nhập a = '))
b = float(input('Nhập b = '))
c = float(input('Nhập c = '))
print('Giải phương trình {}x^2 + {}x + {} = 0'.format(a, b, c))

if(a!=0):
    delta = b**2 - 4*a*c
    if delta < 0:
        print('phương trình vô nghiệm')
    elif delta == 0 :
        x = -b/(2*a)
        print('có nghiệm kép x1=x2=', x)
    else: 
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print('phương trình có nghiệm x1={}, x2={}'.format(x1, x2))           
else:
    print('Không phải phương trình bậc 2')    
