"""Tuple
    - Tuple là 1 chuỗi các phần tử có thứ tự giống như 1 list.
      Sự khác biệt duy nhất là bộ giá trị là các hằng số.
      Tuple một khi được tạo ra thì giá trị của nó không thể sửa đổi.
    - Tuple được sử dụng để bảo vệ dữ liệu và thường nhanh hơn danh sách
      vì chúng không thể thay đổi động 
    - Giá trị của tuple có thể bị trung lặp 
"""
gioiTinh = ('nam', 'nữ')
lopHoc = (1,2,3,4,5,6,7,8,9,10,11,12)
color = ('red', 'green', 'green', 'yellow', 'blue')

# Các thao tác với tuple 
# Truy cập thông qua chỉ mục 
print(gioiTinh[0]) # nam 
print(lopHoc[0:2]) # (1,2)

#lopHoc[0] = 13 #error: 'tuple' object does not support item assignment

# Duyệt 
for x in color:
    print(x)

# Cộng 2 tuple 
y = (1,2,3) + (3,4,5,6)
print(y) #(1, 2, 3, 3, 4, 5, 6)

# Nhân bản tuple 
y = (1,2,3)*3
print(y) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

# Kiểm tra tồn tại 
print('red' in color)

# Số lượng phần tử 
len(color)

# Đếm số luọt xuất hiện 
color.count('green') 

# Tìm min/max, tính sum 
print(min(lopHoc)) #số 
print(min(gioiTinh)) #anphab 
print(max(color)) #yellow 
print(sum(lopHoc))

# Sắp xếp tuple và chuyển về list 
print(sorted(color)) #['blue', 'green', 'green', 'red', 'yellow'] 