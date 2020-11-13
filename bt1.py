# function 
Pi = 3.14
def sum(a, b):
    return a + b

print(sum(1, 2))
# hàm có 2 loại có giá trị trả về và không có giá trị trả về
# hàm thì có nhiều hoặc ko có đối số truyền vào
# hàm chỉ chạy khi gọi 
#vi du ham ko có đối số 

def soPi():
    return 3.14 

pi = soPi()
print (pi)

# viet ham tinh tong s = 1 + 2 + 3 + n
def sumOfN(n): # n la biet local
    s = 0 
    i = 0 
    while i <= n:
        s += i
        i += 1
    return s 
print(sumOfN(5))

# có 2 loại biết là toàn cục(global) và biến địa phương (local)
# biến local thì nó chỉ hoạt động trong phạm vi khai báo (vòng lặp hoặc hàm)
# biến global thì dùng ở khắp nơi trong chương trình
def calculateCircle(r):
    return 2*Pi*r

print (calculateCircle(5))
# viet ham tinh tong so chan  s = 2 + 4 + 6 + 8 + .. + n
def sumOfEvenNumber(n):
    return n
# btvn, ve so do khoi cac bai da hoc, va viet lai bang function
# tinh tong cac chu so cua 1 so co 3 chu so
# n = 123 = 6

def anyNumber(n):
    num = str(n)
    s = 0 
    i = 0
    while i < len(num):
        s += int(num[i])
        i += 1
    return s
key = "k"

# while key == 'k':
#     print ('Please enter a number')
#     num = int(input())
#     print('Sum of ' + str(num) + ' is')
#     print(anyNumber(num))
#     print('press k to continue and press any keywork to exit')
#     key = input()
print ('start print at here')
# bt: in ra cac so chinh phuong tu 1 den 50
# doc lai bai cu, tao 1 file rieng xong code lai
# nhap vao 1 so n, in ra cac uoc so cua no # 9 co uoc la 1 va 3, 9
# nhap 2 so a, b tim uoc chung lon nhat cua 2 so
# nhap 1 so co 3 chu so, in ra do có phải là số dối xứng ko, ví dụ: 101, 303

def compareNumber(n):
    a = n // 100
    b = n % 10
    if (a == b):
        print('true')
    else:
        print('false')
    
compareNumber(535)
# nhap vao 1 so n, kiem tra xem n co phai la so nguyen to ko
def checkPrime(n):
    isPrime = True
    i = 2
    while (i < n):
        if (n % i == 0):
            isPrime = False
            break
        i += 1
    return isPrime
print(checkPrime(7))

def printSeriPrime(n):
    i = 2
    while (i <= n):
        if (checkPrime(i)):
            print(i)
        i += 1
# printSeriPrime(100)
