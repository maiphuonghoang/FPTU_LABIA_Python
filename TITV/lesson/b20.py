# Chuỗi 1 dòng 
s1 = 'Mai'
s2 = 'Phương'
print(s1 + s2 ) #MaiPhương
print(s1 , s2 ) #Mai Phương
print(s1 , s2, sep = "" ) #MaiPhương

# Chuỗi nhiều dòng 

chuoi_nhieu_dong = '''
    Mai
    Phương
    Hoàng 
'''
print(chuoi_nhieu_dong)

# Nhân chuỗi 
chep_phat = 'Em hứa làm bài tập đầy đủ \n'
chep_phat_10 = chep_phat * 10
print(chep_phat_10)

# Chuỗi con 
chuoi_1 = 'maiphuonhoang'
chuoi_2 = 'mai'
if chuoi_2 in chuoi_1 :
    print(chuoi_2,'là con của',chuoi_1)

# Các hàm với chuỗi 
# Viết hoa chữ đầu của từ đầu tiên 
s = "hôm nay thật buồn"
s = str.capitalize(s)

# Viết hoa/thường toàn bộ chuỗi 
s = s.upper()
print(s.lower())

# Tìm chuỗi con 
s = 'hoang mai phuong maiphuonghoang'
print(s.find('a')) #2 Trả về vị trí đầu tiên 
print(s.find('d')) # Trả về -1 nếu k tìm thấy 

# Đếm số lượng chuỗi con 
print(s.count('mai')) # 2 
print(s.count('d')) # 0 

# Lấy chuỗi con 
print(s[0:11])

# Thay thế 
s.replace('phuong', 'PHUONG')
print(s) # không thay đổi 
# phải gán mới thay đổi vì string trong python là immutable 
s = s.replace('phuong', 'PHUONG') #
print(s) # đã thay đổi 

# Cắt chuỗi thành 1 list 
print(s.split(' ')) # ['hoang', 'mai', 'PHUONG', 'maiPHUONGhoang']

# format string
s = '{}{}{}'.format('mai', 1, 2)
print(s)
  




