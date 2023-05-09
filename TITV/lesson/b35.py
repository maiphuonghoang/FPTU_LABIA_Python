"""
    try:
        Đoạn code dự đoán có lỗi
    except:
        Hành động khi lỗi xảy ra 
    else:
        Thực thi đoạn này nếu như mã không có lỗi 
    finally: 
        Cho phép thực thi mã, 
        bất kể kết quả của các khối try có bị lỗi hay không 
"""
try:
    a = int(input('Nhập vào số nguyên a: '))
    print(str(a)+ ' + 5 = ' + str(a+5))
except Exception as e:
    print(e)
# except:
#     print('Nhập sai input')
else:
    print('Không có lỗi xảy ra')
finally:
    print('Kết thúc chương trình')
