# Sử dụng vòng lặp while khi chúng ta không biết trước số lần lặp 

n = -1
while(n <= 0 ):
    n = int(input('Nhập vào n:' ))

j = 0
while (j <= 10):
    print(j, 'Bên trong vòng lặp')
    j += 1
    if j >= 5:
        break
else:
    print(j, 'Bên ngoài vòng lặp')
