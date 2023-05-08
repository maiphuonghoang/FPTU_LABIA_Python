"""OOP
    1. Object
    2. Class
    3. Method 
    4. Inheritance 
    5. Polymorphism 
    6. Encapsulation 
    7. Data Abstraction
"""
# CLASS 
class SimpleClass:
    # Atrribute
    i = 5
    # _init_  
    def __init__(self) :
        self.j = 7
    # methods
    def printMe(self): 
        print(self.j)

objectA = SimpleClass() 
objectB = SimpleClass() 

objectA.printMe()
print(objectB.j)    

# Thay đổi giá trị của thuộc tính 
objectA.i = 100
print(objectA.i)    


# STATIC METHOD
class SimpleClass2:
    # constructor
    def __init__(self) :
        self.name = 'Phương'
    
    def hello(self):
        print('Hello ' + self.name)
    
    # static methods
    @staticmethod
    def hi(name):
        print('Hi ' + name)

objectC = SimpleClass2()
objectD = SimpleClass2()
objectC.hello()
objectC.hi('Peter')
SimpleClass2.hi('static')

"""Xây dựng class Ngày
    - int ngay 
    - int thang
    - int nam 
    + int ngayTrongNam(self)
    + staticmethod int kiemTraSoNgayCuaThang(thang, nam)
"""
class Ngay:
    def __init__(self, giatri_ngay, giatri_thang, giatri_nam):
        self.ngay = giatri_ngay
        self.thang = giatri_thang
        self.nam = giatri_nam

    # xác định số ngày của tháng 
    @staticmethod
    def soNgayCuaThang(thang, nam):
        if(thang in [1,3,5,7,8,10,12]): return 31
        elif(thang in [4,6,9,11]): return 30
        elif(thang == 2):
            # return ((nam % 400 == 0) || (nam % 4 == 0 && (nam % 100 != 0))) ? 29:28
            if(nam % 400 == 0 or (nam % 4 == 0 and (nam % 100 != 0))): 
                return 29
            else: return 28

    # 15/3/2022
    # Tháng 1: 31 ngày 
    # Tháng 2: 28 ngày 
    # 31 + 28 + 15 = ? 
    def ngayTrongNam(self):  
        giaTriNgayTrongNam = 0
        # Tính tổng số lượng ngày của những tháng trước 
        for x in range(1, self.thang):
            giaTriNgayTrongNam += self.soNgayCuaThang(x, self.nam)
            print(str(x)+ " : " + str(self.soNgayCuaThang(x, self.nam)))
        # Cộng thêm số ngày của tháng hiện tại 
        giaTriNgayTrongNam += self.ngay
        #Trả kết quả 
        return giaTriNgayTrongNam
    
ngayA = Ngay(15,9,2022)
print(ngayA.ngayTrongNam())
