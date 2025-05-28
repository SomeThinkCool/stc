'''
- Tong cac so chan/le chia het cho 2
- Fibonacci
- UCLN
- BCNN
- Kiem tra so nguyen to
- Day so nguyen to nho hon n
'''
# Tong cac so chan/le chia het cho 2
def tongchan(a):
    tong=0
    for i in a.split(" "):
        so=int(i)
        if so%2==0:
            tong+=int(i)
    print(f"Tong cac phan tu chia het cho 2: {tong}")

# a = input("Nhap 1 mang: ")
# tongchan(a)

def tongle(b):
    tong = 0
    for i in b.split(" "):
        so = int(i)
        if so % 2 != 0:
            tong += int(i)
    print(f"Tong cac phan tu chia het cho 2: {tong}")

# b = input("Nhap 1 mang: ")
# tongle(b)

# Fibonacci
def day_fibonacci(n):
    print("Day so fibonacci")
    dayso =[]
    i = 0
    while i <= n:
        if i == 0:
            dayso.append(0)
        elif i == 1:
            dayso.append(1)
        else:
            dayso.append(dayso[i-1] + dayso[i-2])
        i += 1
    dayso.pop(0)
    print(f"Day so fibonacci {dayso}")
    print(f"So fibonacci nho nhat : {dayso[0]}")
    print(f"So fibonacci lon nhat : {dayso[n-1]}")

# n = int(input("Nhap vao 1 so nguyen : "))
# day_fibonacci(n)

# UCLN
def ucln(a, b):
    if a == 0 or b == 0:
        return a + b
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

# BCNN
def bcnn(a, b):
    return a*b/ucln(a,b)

# a=int(input("Nhap so a: "))
# b=int(input("Nhap so b: "))
# print("UCLN cua a va b: ", ucln(a,b))
# print("BCNN cua a va b: ", bcnn(a,b))

# Kiem tra so nguyen to
def kt_snto(n):
    if n<2:
        return False
    for i in range (2,n):
        if n%i==0:
            return False
    return True

# Day so nguyen to nho hon n
def day_snto(n):
    ds=[]
    for i in range (2,n):
        if kt_snto(i):
          ds.append(i)
    return ds

# n=int(input("Nhap 1 so nguyen: "))
# print(kt_snto(n))
# print(day_snto(n))






