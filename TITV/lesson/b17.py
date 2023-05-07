# Tạo list rỗng
emptyList1 = []

# Tạo ra một đối tượng List 
emptyList2 = list()

print(emptyList1, emptyList2)

# Tạo ra list có dữ liệu 
colors = ['red', 'green', 'green', 'yellow'] 
print(colors[:])
print(colors[0:2]) # list([x:y]) -> lấy ra [x, y)
print(colors[0], colors[1], colors[2])
print(colors) 

# Thêm phần tử vào list 
colors.append('blue') #thêm vào cuối 
colors[len(colors):] = ['pink']
colors.insert(2, 'black') #chèn vào vị trí 
print(colors) 

# Số lượng phần tử có trong list 
print(len(colors))

# Đếm số lượng phần tử thỏa điều kiện 
print('đếm red =', colors.count('red'), 'đếm green =', colors.count('green'))

# Xóa phần tử khỏi list bằng giá trị 
colors.remove("green") # xóa phần tử đầu tiên có giá trị truyền vào 

#Kiểm tra phần tử có trong list 
if 'black' in colors :
    colors.remove('black') 

# Xóa phần tử khỏi list bằng vị trí 
colors.pop(0)
colors.pop(len(colors) - 1)

# Đảo ngược list 
colors.reverse()

# Sắp xếp list  
colors.sort()
print(colors) 
numbers = [7,5,1,9,0]
numbers.sort(reverse=True)
print(numbers)

# Xóa sạch dữ liệu trong list 
colors.clear()










