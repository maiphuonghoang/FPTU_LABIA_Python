"""Dictionary
    - Từ điển được sử dụng để lưu trữ các giá trị dữ liệu trong các cặp key:value 
    - Từ điển là một tập hợp được sắp xếp theo thứ tự, có thể thay đổi 
      và không cho phép trùng lặp 
    - Từ điển có thể thay đổi, nghĩa là chúng có thể thay đổi , thêm hoặc bớt các mục 
      sau khi từ điển đã được tạo 
"""
sinhVien ={
    'hoVaTen': 'Nguyen Van A',
    'maLop': 'DH01', 
    'diemTrungBinh': 8.5,     
}
print(sinhVien)
# Lấy giá trị 
print(sinhVien['hoVaTen'])
print(sinhVien.get('maLop'))

# Cập nhật giá trị 
sinhVien['maLop'] = 'DH02' 
sinhVien.update({'maLop':'DH03'})
sinhVien.update({
    'hoVaTen': 'Nguyen Van B',
    'maLop': 'DH05', 
})

# Thêm cặp key-value mới 
sinhVien['namHoc'] = 2023
sinhVien.update({
    'noiSinh': 'Ha Noi',
})

# Loại bỏ các mục 
"""
    pop(): loại bỏ mục có tên khóa được chỉ định 
    popitem(): xóa mục được chèn cuối cùng 
    del: khóa loại bỏ mục có tên khóa được chỉ định, hoặc toàn bộ từ điển  
    clear(): làm trống từ điển 
"""
print(sinhVien) #{'hoVaTen': 'Nguyen Van B', 'maLop': 'DH05', 'diemTrungBinh': 8.5, 'namHoc': 2023, 'noiSinh': 'Ha Noi'}
sinhVien.pop('noiSinh')#{'hoVaTen': 'Nguyen Van B', 'maLop': 'DH05', 'diemTrungBinh': 8.5, 'namHoc': 2023}
sinhVien.popitem()#{'hoVaTen': 'Nguyen Van B', 'maLop': 'DH05', 'diemTrungBinh': 8.5}
del(sinhVien['maLop'])#{'hoVaTen': 'Nguyen Van B', 'diemTrungBinh': 8.5}
sinhVien.clear() #{}
del(sinhVien) ;#print(sinhVien)#name 'sinhVien' is not defined



sinhVien ={
    'hoVaTen': 'Nguyen Van A',
    'maLop': 'DH01', 
    'diemTrungBinh': 8.5,     
}
# In tất cả các tên khóa trong từ điển
# for x in sinhVien :
#     print(x)
'''
hoVaTen
maLop
diemTrungBinh
'''

# Duyệt các giá trị 
for x in sinhVien.values():
    print(x)
'''
Nguyen Van A
DH01
8.5
'''

# Duyệt các khóa 
for x in sinhVien.keys():
    print(x)






