for i in range(10):
    print(i)
    if(i>5): break
n = 100
while n > 0 :
    print(n)
    n = n // 2
    if(n < 50): break

""" continue
    Sử dụng để bỏ qua phần còn lại bên trong vòng lặp của lần lặp hiện tại.
    Vòng lặp không kết thúc mà tiếp tục với lần lặp tiếp 
"""
# in ra các số chẵn 
for i in range(10):
    if(i%2==1): continue
    print(i)