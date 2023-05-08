

'''
# Ví dụ set
    - Mã căn cước công dân
    - Biển số xe 
    - Số điện thoại 

#   Xây dựng chương trình rút thăm trúng thưởng với các chức năng
    1. Thêm một mã số dự thưởng vào thùng
    2. Xóa một mã số dự thưởng ra khỏi thùng
    3. Quay số ngẫu nhiên lấy ra một mã số trúng thưởng 
'''

# Thư viện random 
import random 

# Khai báo set 
thungPhieu = set()

# Vòng lặp 
while True:
    menu = '''
    --------------------- Menu ----------------------
    Vui lòng lựa chọn chức năng 
    1. Thêm một vào thùng phiếu dự thưởng
    2. Xóa một số điện thoại dự thưởng ra khỏi thùng
    3. Quay số ngẫu nhiên lấy ra một số điện thoại trúng thưởng 
    4. Kết thúc   
    '''    
    print('Thùng phiếu hiện tại', thungPhieu)
    print(menu)
    luaChon = int(input('Lựa chọn: '))

    if luaChon == 1:
        soDienThoai = input('Nhập vào số điện thoại dự thưởng: ')
        thungPhieu.add(soDienThoai)
    elif luaChon == 2:
        soDienThoai = input('Nhập vào số điện thoại dự thưởng: ')
        thungPhieu.discard(soDienThoai)
    elif luaChon == 3:
        index = random.randint(0, len(thungPhieu) - 1)
        print('Vị trí trúng thưởng: '+ str(index))
        i = 0
        for x in thungPhieu:
            if(i == index):
                break
            i += 1
        print('Số điện thoại', x, 'đã trúng thưởng')        
        thungPhieu.discard(x)
    else :
        break

    x = input('Nhập phiếu bất kì để tiếp tục')

