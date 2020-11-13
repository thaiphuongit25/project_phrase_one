# thuật toán
# thuật toán tìm kiếm tuyến tính: 
# bài toán: cho 1 mảng a và 1 số n, tìm kiếm xem n có thuộc mảng a không
a = [1, 4, 6, 7, 9, 20, 10]
n = 4

# xây dựng hàm 
def searchLearning(a, n):
    isRight = False
    for item in a:
        if (item == n):
            isRight = True
            break
    return isRight

#print(searchLearning(a, n))
# Tim kiếm nhị phân: áp dụng cho 1 mảng đã được sắp xếp 
# b1 : lấy điểm giữa 
# b2: kiểm trả n có bằng a[mid] không, nếu bằng trả về true
# b3: kiểm tra nếu n < a[mid] thì tìm kiếm trong khoảng từ a[0] đến a[mid - 1]
# b4: Nếu n > a[mid] thì kiểm tra trong khoảng từ a[mid + 1] đến a[len(a) - 1]
a = [1, 3, 5, 6, 8, 10, 12]
n = 5

def searchBinary(a, n):
    isRight = False
    mid = len(a) // 2
    if (n == a[mid]):
        isRight = True
    elif n < a[mid]:
        i = 0
        while i <= (mid - 1):
            if (n == a[i]):
                isRight = True
                break
            i += 1
    else:
        j = mid + 1 
        while j <= (len(a) - 1):
            if (n == a[j]):
                isRight = True
                break
            j += 1
    return isRight

print  (searchBinary(a, n))

# btvn: kiem tra 1 so có phải la so hoan hảo ko: là số có tổng bằng các ước số của nó 
# ví du: 6 = 3 + 2 + 1 
# bt1 nhap vao 1 so n, kiem tra xem n có phải là số hoàn hảo ko
# bt2 in ra day số hoàn hảo từ 1 đến 1000
