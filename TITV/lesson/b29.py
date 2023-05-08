
# Khi không xác định được đối số, chúng ta có thể sử dụng dấu *
def thoiKhoaBieu(*monHoc):
    print('Mon 1: ' + monHoc[0])
    print('Mon 2: ' + monHoc[1])

thoiKhoaBieu('Toan', 'Ly', 'Van')

def tinhTong(*giaTri):
    sum = 0
    for x in giaTri:
        sum += x
    print('Sum: ', sum)
tinhTong(1,4,5,6) 

# Truyền nhiều đối số, xác định thông qua tên, sử dụng **
def xinChao(**hoVaTen ):
    print('Xin chao: ' + hoVaTen['ho'])
xinChao(ten='Phương', dem="Mai", ho='Hoàng')

# Sử dụng từ khóa return để trả về giá trị 
def tinhTich(*giaTri):
    tich = 1
    for x in giaTri:
        tich *= x
    return tich
print(tinhTich(1,2,3,10))
print(tinhTich(1))

'''
    Tìm UCLN của 2 số tự nhiên a, b
    Xây dựng hàm: gcd(a, b) => trả về UCLN 
    VD: gcd(1,13)=1; gcd(35,77)=7
    Thuật toán: 
    35, 42        77-35
    35, 7
    28, 7
    21, 7
    14, 7
    7,  7 
'''

def gcd(a, b):
    while (a != b):
        if(a>b): a = a - b 
        else: b = b - a
    return a
print('gcd({},{}) = {}'.format(1,13, gcd(1, 13)))
print('gcd({},{}) = {}'.format(35,77, gcd(35, 77)))

def lcm(a, b):
    timeA = a
    timeB = b 
    while (a != b):
        if(a>b): b += timeB
        else: a += timeA
    return a
print('lcm({},{}) = {}'.format(2,6, lcm(2, 6)))
print('lcm({},{}) = {}'.format(7,9, lcm(7, 9)))

"""
    Nhập vào 1 dãy (n) số từ bàn phím, sau đó tính tổng 
        nhap(n, list_number)
        tinhTong(list_number)
"""
list_number = []
def nhap(n):
    for i in range(n):
        x = int(input('n{} = '.format(i)))
        i+=1
        list_number.append(x)
nhap(int(input('Nhập số lượng phần tử trong dãy: ')))
print('list_number: ' , list_number)

def tinhTong(numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum 
print('tinhTong: ' ,tinhTong(list_number))



