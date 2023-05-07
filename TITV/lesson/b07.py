""" Các kiểu dữ liệu cơ bản trong Python
    Python là một ngôn ngữ thông dịch (không yêu cầu biên dịch), được đặc trưng 
    bởi hệ thống kiểu động - bạn không bắt buộc phải khai báo kiểu của biến.
    Trình thông dịch tự đoán kiểu dữ liệu.  

KIỂU DỮ LIỆU        MÔ TẢ                   VÍ DỤ 
    int             số nguyên               x = 1
    float           số thực                 x = 2.3
    complex         số phức                 x = 1 + 2j
    bool            Boolean: True/ False    x = True  
    str             String: chuỗi kí tự     x = 'abc'
    NoneType        Đối tượng đặc biệt      x = None 
                    chỉ ra giá trị null        
"""

# Cách kiểm tra kiểu dữ liệu của biến: type()
print(type(1), type(2.3), type(1 + 2j), type('abc'), type(False), type(None))
#<class 'int'> <class 'float'> <class 'complex'> <class 'str'> <class 'bool'> <class 'NoneType'>