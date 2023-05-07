"""
    - Một số hàm quan trọng 
    math.ceil(x)        Trả về giá trị trần của x, số nguyên nhỏ nhất >= x
    math.floor(x)       Trả về sàn của x, số nguyên lớn nhất <= x
    math.fabs(x)        Trả về giá trị tuyệt đối của x
    math.exp(x)         Trả về e lũy thừa x, trong đó e = 2.7182 là cơ số của logarit tự nhiên 
    math.log(x, base)   Trả về logarit tự nhiên của x (cơ số e)
    math.pow(x, y)      Trả về x lũy thừa y 
    math.sqrt(x)        Trả về căn bậc 2 của x  

    - Một số giá trị constants
    math.pi 
    math.e 

"""

import math 

x = float (input("x: "))
print("|x| = ", math.fabs(x))
print("sqrt(x) = ", math.sqrt(x))
print("log = ", math.log(x,2))

