""" Set
    - Set là tập hợp không có thứ tự, không thể thay đổi và không được lặp chỉ mục
    - Giá trị không được trùng nhau 
    - Lưu ý: các mục set là không thể thay đổi, nhưng có thể xóa các mục và thêm các mục mới 
"""

monHoc = {'Toán', 'Lý', 'Hóa'}

# Duyệt phần tử 
for x in monHoc: print(x)

# Thêm mới 
# Thêm 1 phần tử 
monHoc.add('Lịch sử')
# Thêm 1 tập hợp khác 
hocthem = {'Anh', 'Piano'}
monHoc.update(hocthem)
# Thêm list vào set 
hocPhuDao = ['Võ', 'Múa', 'Võ']
monHoc.update(hocPhuDao) # k lấy trùng 

# Xóa phần tử
"""
    - remove(): nếu phần tử không tồn tại sẽ phát sinh lỗi.
    - discard(): nếu phần tử không tồn tại sẽ không phát sinh lỗi.
    - pop(): loại bỏ phần tử đầu tiên 
    - clear(): làm rỗng tập hợp 
    - Xóa bỏ tập hợp bằng từ khóa del 
"""

#print(monHoc.remove('Võ')) #None 
monHoc.remove('Võ'); print(monHoc)
#monHoc.remove('Sinh') #error 
monHoc.discard('Sinh'); print(monHoc)

#{'Lý', 'Piano', 'Múa', 'Hóa', 'Anh', 'Toán', 'Lịch sử'}
print(monHoc.pop()) #Lý , poptrả về phần tử đầu 
print(monHoc) #{'Piano', 'Múa', 'Hóa', 'Anh', 'Toán', 'Lịch sử'}

monHoc.clear(); print(monHoc) #set()

del monHoc #Xóa biến 
print(monHoc) #NameError: name 'monHoc' is not defined



