"""
    + - * / 
    **  Mũ 
    %   Chia lấy phần dư 
    //  Chia lấy phần nguyên 
"""

a = input('Nhập vào số a: ') # str 
b = input('Nhập vào số b: ') # str

a = int(a); b = int(b)

print("{0} + {1} = {2}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))