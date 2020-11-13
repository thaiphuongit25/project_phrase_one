# sap xep 1 mang tang, giam dan
# bt: tim so lon nhat, nho nhat trong 1 mang

# btvn: in chuổi fibonaxi từ 1 đến 1000
# 
# chuoi fibonaci : 1, 1, 2, 3, 5, 8

def fibonaci(n):
    n1, n2 = 0, 1
    nth = 0
    i = 0
    while i <= n:
        print (n1)
        nth = n1 + n2 
        n1 = n2 
        n2 = nth 
        if(nth > 100):
            break
        i += 1

fibonaci(10)
# tính tổng s = 1*1 + 2*2 + .. + n*n
