'''
- Dem so tu trong 1 cau da nhap
- Dem so ki tu trong doan
- GPTB2
- So chinh phuong
- So hoan hao
'''
import math
# Dem so tu trong 1 cau da nhap
def dem_so_tu():
    n=input("Nhap 1 cau: ")
    bo_cach=n.split(" ")
    kq=len(bo_cach)
    print("So tu trong cau la: ",kq)

# dem_so_tu()

# Dem so ki tu trong doan
def dem_so_ki_tu():
    n=input("Nhap: ")
    dodai=len(n.replace(" ",""))
    print(dodai)

# dem_so_ki_tu()

# GPTB2
def gptb2(a,b,c):
    delta = pow(b,2)-4*a*c
    if (delta < 0):
        print("Phuong trinh vo nghiem")
    elif (delta == 0):
        print(f"Phuong trinh tren co nghiem kep x1=x2={-b/2*a}")
    else:
        print(f"Phuong trinh co 2 nghiem phan biet x1 = {-b+math.sqrt(delta)/2*a} , x2 = {-b-math.sqrt(delta)/2*a}")

# a = float(input("Nhap a : "))
# b = float(input("Nhap b : "))
# c = float(input("Nhap c : "))
# print(gptb2(a,b,c))

# So chinh phuong
def kt_scp(n):
    can=int(math.sqrt(n))
    if can*can==n:
        return True
    return False
def day_so_cp(n):
    ds=[]
    for i in range (0,n):
        if kt_scp(i):
            ds.append(i)
    return ds

# n=int(input("Nhap 1 so nguyen: "))
# print(kt_scp(n),day_so_cp(n))

# So hoan hao
def kt_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
    if tong == n:
        return True
    else:
        return False
def day_shh(n):
    ds=[]
    for i in range (1,n):
        if kt_so_hoan_hao(i):
            ds.append(i)
    return ds

# n=int(input("Nhap 1 so nguyen: "))
# print(kt_so_hoan_hao(n),day_shh(n))

