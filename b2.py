'''
Xay dung CT Quan ly Ban hang
Yeu cau:
1. Xay dung cac lop:
    - Customer (Khachhang): Gom Makh, Tenkh, Diachi, Sdt, Soluong, Dongia
2. Ap dung ke thua:
    - Tao lop VIPCustomer ke thua Customer, them thuoc tinh Mucchietkhau
    - Khi khach VIP mua hang, tinh tong tien sau khi ap dung chiet khau
3. Cac chuc nang yeu cau:
    - Nhap 1 danh sach khach vip
    - Hien thi danh sach don hang va tong tien tung don hang
    - Tinh tong doanh thu trong ngay
4. Ghi danh sach khach hang len 1 tep
'''
import pickle
class Customer:
    def __init__(self):
        self.Makh=" "
        self.Tenkh=" "
        self.Diachi=" "
        self.Sdt=" "
        self.Soluong=0
        self.Dongia=0.0
    def input(self):
        self.Makh=input("Nhap ma KH: ")
        self.Tenkh=input("Nhap ten KH: ")
        self.Diachi=input("Nhap dia chi: ")
        self.Sdt=input("Nhap SDT: ")
        self.Soluong=int(input("Nhap so luong: "))
        self.Dongia=float(input("Nhap don gia: "))
    def output(self):
        print("Ma KH: ",self.Makh)
        print("Ten KH: ",self.Tenkh)
        print("Dia chi: ",self.Diachi)
        print("Sdt: ",self.Sdt)
        print("So luong: ",self.Soluong)
        print("Don gia: ",self.Dongia)

class VIPCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.Mucchietkhau=0.0
    def input(self):
        super().input()
        self.Mucchietkhau=float(input("Nhap muc chiet khau: "))
    def output(self):
        super().output()
        print("Muc chiet khau: ",self.Mucchietkhau,"%")
        print("Tong tien: ",self.Tongtien())
    def Chietkhau(self):
        return self.Soluong*self.Dongia*self.Mucchietkhau/100
    def Tongtien(self):
        return (self.Soluong*self.Dongia)-self.Chietkhau()

def ghi(name,dsvip):
    with open(name, "wb") as f:
        pickle.dump(dsvip,f)
def doc(name):
    with open(name,"rb") as f:
        return pickle.load(f)

def main():
    ds=[]
    n=int(input("Nhap so luong khach VIP: "))
    for i in range(n):
        print(f"\nNhap thong tin khach VIP {i+1}: ")
        vip=VIPCustomer()
        vip.input()
        ds.append(vip)
    ghi("/home/tuyen/ds.dat",ds) #D:\\ds.dat
    print("\n--- Danh sach da duoc ghi vao tep ---")
    dsvip=doc("/home/tuyen/ds.dat")
    sum=0
    for vip in ds:
        print("==========================")
        vip.output()
    for vip in ds:
        sum+=vip.Tongtien()
    print("==========================")
    print("Tong doanh thu trong ngay: ",sum)
if __name__ == "__main__":
    main()
