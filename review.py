# print ('hello')
# # variable
# s = 'sdfd'
# # data type: integer, float, string, boolean, array, object hash.
# i = 1
# s = "sdf"
# b = True 
# atr = [1, 2, 3]
# arrayObject = [{"name": "tuan", "toan": 8}]
# # thao tac voi so: + - * /, // -> chia nguyen, %s
# # thao tac voi chuoi: s1 = "a" s2 = "b" s = s1 + s2
# # str = "hello" str[0] str[-1]
# # thao tac voi mang: a = [], b = 1, a.append(b)
# # cau lenh if
# a = 3
# if (a >0):
#     print ('a so duong')
# else:
#     print ('a la so am')
# # while : con lap cho den khi dieu kien con ok
# while a > 0:
#     print (a)
#     a -= 1
# # for : duyet qua tung phan tu trong mang
# atr = [1, 2, 3, 4, 5]
# for item in atr:
#     print (item)
# # break: break vong lap va thoat
# # tinh tong s = 1 + 2 + 3 + .. + n
# # function, bat dau 
# def sum(a, b):
#     return a + b
# c = sum(2, 3)

# def prinSerialNumber(n):
#     for item in n:
#         print (item)

# viet ham so tinh tong s = 2 + 4 + 6 + .. + n (neu n chan) n - 1 (neu n le)
# nhap vao 1 so n, kiem tra xem so do co phai so nguyen to ko, viet ham tra ve True, False
def isPrime(n):
    isRight = True
    a = 2
    while a <= n // 2:
        if n%a == 0:
            isRight = False
            break
        a += 1
    return isRight
# in ra chuoi cac so nguyen to tu 1 den 100

#print(isPrime(5))

def printPrime(n):
    j = 2
    while j <= n:
        if (isPrime(j)):
            print(j)
        j += 1

printPrime(100)

print('hello')

# btvn 
# bt1: viet ham kiem tra 1 so co phai la so hoan hao vd: 6 = 1 + 2 + 3
# bt2: in ra cac so hoan hao tu 1 den 100sd
