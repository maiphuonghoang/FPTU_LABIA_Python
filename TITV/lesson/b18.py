n = 10
sum = 0
for i in range (n) :
    print(i)
    sum += i
print(sum)

# Vòng lặp for có bước tăng tùy chỉnh 
#bắt đầu, kết thúc, bước tăng  
for i in range (2, 10, 2) :
    print(i)
for i in range (10, 0, -2) :
    print(i)

# Vòng lặp for duyệt các phần tử của list
colors = ['red', 'green', 'green', 'yellow'] 
for color in colors :
    print(color)

# Vòng lặp for duyệt các phần tử theo vị trí 
for i in range(len(colors)) :
    print(colors[i])

"""Bài tập in bảng cửu chương"""
for i in range(2, 10):
    print('bảng cửu chương', i)
    for j in range(1, 11):
        print("{} * {} = {}".format(i, j, i*j))