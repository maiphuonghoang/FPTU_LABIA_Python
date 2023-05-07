'''Biến
    - Chúng ta có thể sử dụng các chữ cái (a-z, A-Z), các con số (0-9),
    dấu gạch dưới _ để đặt tên cho biến hoặc hằng số
    - Tên không bắt đầu bằng số
    - Không sử dụng từ khóa làm tên biến hoặc hằng số (True, False, and, class, global,...)

'''
# Gán giá trị cho 1 biến 
x = 5; print(x)
my_full_name = 'maiphuonghoang'; print(my_full_name)

# Gán giá trị cho nhiều biến
x, y, z = 1, 2, 'A'
print (x, y, z)

# Gán giá trị cho nhiều biến có giá trị giống nhau 
x = y = z = 1; print(x, y, z)

'''Hằng số
    Trong python thực sự không có hằng số 
    Hằng số thường được khai báo và gán trong một mô-đun và người dùng hạn chế không thay đổi 
    giá trị của nó. Ở đây, mô-đun là một tệp mới chứa các biến, hàm,... được nhập vào tệp chính.
    Bên trong module, các hằng số được viết bằng tất cả các chữ cái in hoa và dấu gạch dưới 
    ngăn cách các từ 
'''
PI = 3.14; print(PI)
PI = 3.1415; print(PI)

import math
print(math.pi)




