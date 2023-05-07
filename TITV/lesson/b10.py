"""Toán tử so sánh 
    >   <   ==  <=  >=  !=  
"""

a = input('Nhập vào số a: ')  
b = input('Nhập vào số b: ') 

a = int(a); b = int(b)

print("{0} < {1} là {2}".format(a, b, a < b))
print("{} > {} là {}".format(a, b, a > b))
print("{} <= {} là {}".format(a, b, a <= b))
print("{} >= {} là {}".format(a, b, a >= b))
print("{} == {} là {}".format(a, b, a == b))
print("{} != {} là {}".format(a, b, a != b))

'''Toán tử logic 
    and    or   not    
'''
print (True and False) 
print (True or False) 
print (not False) 

"""Toán tử gán 
    += -=  *=  /=  **=  //=  
    &=   !=   ^=   >>=  <<=   
"""

"""Toán tử bit
    &   bitwise AND
    |           OR
    ^           XOR
    ~           NOT
    <<          left shift
    >>          right shift
"""

"""Toán tử đặc biệt
    is      is not 
"""
