print ('hello')
# phep % -> lay so du -> kiem tra so chan le
print (17 % 3)
# kiem tra so a la chan thi in ra so chan, neu la so le in a la so le
a = 5
if (a % 2 == 0):
    print ('a la so chan')
else:
    print ('a la so le')
# 
# nhap vao 1 so in ra binh phuong cua no
c = 4 
print (c**3)
# nhap vao chieu dai, rong cua hinh chu nhat, in ra chu vi va dien tich
d = 4 
r = 6
print ('dien tich la: ' + str(d * r))
print ('chu vi la:' + str())
# string ->chuoi
name = "nam"
print (name)
# thao tac tren chuoi
# cong chuoi
firstname = 'john'
lastname = 'steven'
# in ra ra full name
print (firstname + ' ' + lastname)
# thao tac voi string
# lay chu cai dau tien cua name
print (name[0])
print (len(name))
print (name[1:3])
print (name[-1])
print (name[1:])
# nhap vao chu nghieng , in ra dao nguoic
d = 'nghieng'
print (d[1] + d[0])
d = 'nga'
# bien la gi? noi luu tru du lieu (bien co 2 loai)
# bien hang so -> viet bang chu hoa , ko gan duoc
# bien thuong thi gan duoc
PI = 3.14
print (PI)
name = "abc"
name = "def"
print (name)
# array -> mang -> tap hop nhieu phan tu co kieu du lieu giong hoac khac nhau
toA = ['nam', 'tu', 'phuong']
toB = ['a', 'b', 'c']
stt = [1, 2, 3, 4]
con = [1, 2, 'phuong', 'nam']
# in ra nhung nguoi thuoc to A
print (toA[0] + ' ' + toA[1] + ' ' + toA[2])
# su dung if , nhap vao 1 so n, kiem tra, so do chia het cho 3 in ra 'chia het cho 3', neu chia het cho 5 in ra 'chia het cho 5'
# neu chia het cho ca 3 va 5 in ra chi het cho 3 va 5
n = 15
# 
# nếu < 0 -> số âm, lớn hơn 0 và bé 10 -> số bé, bé 100 lớn 10 -> số trung bình và lớn hơn 100 số lớn
if n < 0:
    print ('số âm')
elif n < 10:
    print ('số bé')
elif n < 100:
    print ('số trung bình')
else:
    print ('số lớn')
# data type: number, string, List (array), boolean (true or false), object -> đối tượng
# một số phép toán: and, or, not -> phủ định
print (1 < 2 and 2 > 3)
print (1 > 2 or 2 < 3)
print (not(1<2))
for item in toA:
    print (item)
for i in range(5):
    print (i)
print ('start ---')
for i in range(1, 5):
    print (i)
# nhập vào vao chuoi, dao chuoi
c = "hello viet nam"
# in day 1 den 10
i = 0
while (i <= 10):
    print (i)
    i = i + 1
print(i)
lc = len(c)
s = ''
i = lc - 1
while (i >= 0):
    s = s + c[i]
    i = i - 1
print(s)
# lc = 14, i = 13, 13 >= 0 ->right, s = '' + 'm' = 'm', i = 12
# i = 12, 12 >= 0 ->right, s = 'm' + 'a' = 'ma', i = 11
# tinh tong s = 1 + 2 + ... + 10
s = 0
i = 1
while (i <= 10):
    s += i #-> s = s + i
    i += 1 # -> i = i + 1
print (s)
# btvn , cho so n = 100, tinh tong cac so chan tu 1 den 100, 
# tinh tong cac so le 
# tinh tong sau s = 1^2 + 2^2 + ... + 10^2

i = 1
s = 0
while i < 10:
    s = s + i**2
    i = i + 1

print(s)
# i = 1, s = 1
# i = 2, s = 1 + 4 = 5
# tinh tong so chan, le
s = 0 
i = 1
l = 0
while i <= 6:
    if (i % 2 == 0):
        s += i
    else:
        l += i
    i += 1
print (s) # tong so chan
print (l) # tong so le

# nhap vao so n = 5
# tinh tong tu 1 den 4
# co 2 cach, dung if or dung break
n = 5
i = 1 
s = 0 
while i <= n:
    s += i
    if (i == 4):
        break
    i += 1
    print(i)
print(s)


