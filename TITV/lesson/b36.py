# open(): mở/tạo file
# "x" . tạo file 
try:
    f = open('vidu1.txt', 'x')
except Exception as e:
    print(e)
finally:
    # đóng file 
    f.close()


try:
    with open('vidu1.txt', "w") as f:
        # "w" - ghi dữ liệu file
        # "a" - nối vào file 
        f.write('Xin chao cac ban')
    with open('vidu1.txt', "a") as f:
        f.write('\nViet tiep vao file')
except Exception as e:
    print(e)
finally:
    f.close()


try:
        # "a" - nối vào file 
    with open('vidu1.txt', "a") as f:
        f.write('\nViet tiep vao file')
except Exception as e:
    print(e)
finally:
    f.close()

# "r" . đọc file
"""
    f.read()    đọc cả file
    f.readLines()   đọc các dòng 
    f.readLine()   đọc 1 dòng 
"""
try:       
    with open('vidu1.txt', "r", encoding='utf-8') as f:
        list_noidung = f.readlines()
        i = 0
        for line in list_noidung:
            print(str(i)+"/" + line)
            i+=1
except Exception as e:
    print(e)
finally:
    f.close()

# encoding = utf-8
try:       
    with open('vidu1.txt', "r", encoding='utf-8') as f:
        noidung = f.read()
        print(noidung)
except Exception as e:
    print(e)
finally:
    f.close()








