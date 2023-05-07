
"""Chuyển đổi kiểu ngầm định
    Python tự động chuyển đổi một kiểu dữ liệu này sang kiểu dữ liệu khác.
    Quá trình này không cần bất kì sự tham gia nào của người dùng.
"""
a = 5; print(type(a)) #int 
b = 2.0; print(type(b)) #float
c = a/b
print(c); print(type(c)) #float
# Python muốn tránh việc làm mất mát dữ liệu => lấy kiểu dữ liệu lớn hơn làm mặc định cho dữ liệu trả về 

a = 5; print(type(a)) #int 
b = 2; print(type(b)) #int 
c = a/b
print(c); print(type(c)) #float

"""Chuyển đổi kiểu dữ liệu rõ ràng 
    Do chúng ta thực gõ lệnh chuyển đổi kiểu dữ liệu của một đối tượng thành 
    kiểu dữ liệu bắt buộc. 
    Sử dụng các hàm có sẵn int(), float(), str(),... để thực hiện chuyển đổi 
    Cú pháp: ten_kieu_du_lieu(biến)
"""

n = 100
m = '200'
print (str(n) + m) # 100200 

n = 100
m = '200'
print (n + int(m)) # 300