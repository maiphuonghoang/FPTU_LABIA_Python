n = -1
while n<=0:
    n = int(input('Nhập vào n>0: '))

# Chuyển từ thập phân sang nhị phân 
ketQua = ''
while (n > 0) :
    # ketQua += str(n % 2)
    ketQua = str(n % 2) + ketQua
    print('n % 2 =', n % 2)
    n = n // 2
    print('n =',n)
print (ketQua)
 