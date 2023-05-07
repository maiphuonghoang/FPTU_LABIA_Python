'''
Nhập 3 điểm trên hệ trục tọa độ Oxy
1. Xác định 3 điểm có tạo thành tam giác
2. Nếu tạo thành tam giác:
    Xuất ra chu vi và diện tích của tam giác 
'''
import math 

# Nhập dữ liệu
xA, yA = float(input('Nhập vào xA: ')), float(input('Nhập vào yA: '))
xB, yB = float(input('Nhập vào xB: ')), float(input('Nhập vào yB: '))
xC, yC = float(input('Nhập vào xC: ')), float(input('Nhập vào yC: '))

# Tính các cạnh 
ab = math.sqrt(math.pow(xB-xA , 2) + math.pow(yB-yA , 2))
bc = math.sqrt(math.pow(xB-xC , 2) + math.pow(yB-yC , 2))
ac = math.sqrt((xC-xA)**2 + (yC-yA)** 2)

if (ab+bc>ac) and (ab+ac>bc) and (ac+bc>ab):
    print('Tam giác có 3 cạnh: ', ab, ac, bc)
    # Tính chu vi 
    cv = ab + ac + bc 
    print ('chu vi = ', cv)
    # Tính diện tích tam giác 
    p = cv/2
    print ('diện tích = ', math.sqrt(p*(p-ab)*(p-bc)*(p-ac)))
else:
    print('Không tạo thành tam giác')
