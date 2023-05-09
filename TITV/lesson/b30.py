"""Lambda 
    lambda arguments : expression 
"""
kiemTraSo = lambda a : ('chẵn' if a%2==0 else 'lẻ')
print(kiemTraSo(10))
print(kiemTraSo(5))

sum = lambda a,b : a+b
print(sum(1,2))

"""Tạo hàm mũ"""
# Ví dụ về sử dụng lambda expression bên trong các function 
def hamMuHai(a):
    return a**2
def hamMuBa(a):
    return a**3

def hamMu(n):
    return lambda x : x**n

hamMu2 = hamMu(2) 
        #  lambda x : x**2
hamMu3 = hamMu(3)
hamMu4 = hamMu(4)

print(hamMu2(3))
print(hamMu3(3))
print(hamMu4(3))


