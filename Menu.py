'''
Đề bài: Xây dựng chương trình Quản lý Bán hàng
Yêu cầu:
1. Xây dựng các lớp:
Customer (Khách hàng):
Gồm các thuộc tính:
Mã khách hàng
Tên khách hàng
Địa chỉ
SĐT
Số lượng
Đơn giá
2. Áp dụng kế thừa:
Tạo lớp VIPCustomer kế thừa từ Customer, thêm thuộc tính:
Mức chiết khấu.
Khi khách VIP mua hàng, cần tính tổng tiền sau khi áp dụng chiết khấu.
3. Các chức năng yêu cầu:
Nhập danh sách khách VIP
Hiển thị danh sách đơn hàng và tổng tiền từng đơn hàng
Tính tổng doanh thu trong ngày
4. Ghi danh sách khách hàng lên 1 tệp (file)
'''

import pickle

class Customer:
    def __init__(self):
        self.makh = ""
        self.tenkh = ""
        self.diachi = ""
        self.sdt = ""
        self.soluong = 0
        self.dongia = 0.0

    def input(self):
        self.makh = input("Nhập mã KH: ")
        self.tenkh = input("Nhập tên KH: ")
        self.diachi = input("Nhập địa chỉ: ")
        self.sdt = input("Nhập số điện thoại: ")
        self.soluong = int(input("Nhập số lượng: "))
        self.dongia = float(input("Nhập đơn giá: "))

    def output(self):
        print(f"Mã KH: {self.makh}")
        print(f"Tên KH: {self.tenkh}")
        print(f"Địa chỉ: {self.diachi}")
        print(f"SĐT: {self.sdt}")
        print(f"Số lượng: {self.soluong}")
        print(f"Đơn giá: {self.dongia:.2f}")
        print(f"Tổng tiền: {self.tong_tien():.2f}")

    def tong_tien(self):
        return self.soluong * self.dongia

class VIPCustomer(Customer):
    def __init__(self):
        super().__init__()
        self.chietkhau = 0.0

    def input(self):
        super().input()
        self.chietkhau = float(input("Nhập chiết khấu (%): "))

    def output(self):
        super().output()
        print(f"Chiết khấu: {self.chietkhau}%")
        print(f"Thành tiền sau chiết khấu: {self.thanh_tien():.2f}")

    def thanh_tien(self):
        return super().tong_tien() * (1 - self.chietkhau / 100)

ds_khach = []

def ghi(name, ds):
    with open(name, 'wb') as f:
        pickle.dump(ds, f)

def doc(name):
    with open(name, "rb") as f:
        return pickle.load(f)

'''
def menu():
    tong=0
    while True:
        print("\n==== MENU QUAN LY KHACH VIP ====")
        print("1. Nhap danh sach khach VIP")
        print("2. Hien thi danh sach don hang")
        print("3. Tinh tong doanh thu")
        print("0. Thoat")

        chon = input("chon chuc nang: ")
        if chon == "1":
            n = int(input("Nhập số khách VIP: "))
            for i in range(n):
                print(f"\nNhập khách thứ {i+1}:")
                vip = VIPCustomer()
                vip.input()
                tong += vip.thanh_tien()
                ds_khach.append(vip)
        elif chon == "2":
            print("\n--- DANH SACH KHACH VIP ---")
            for i, kh in enumerate(ds_khach, 1):
                print(f"\nKhach hang {i}: ")
                kh.output()
        elif chon == "3":
            print(f"tong doanh thu {tong}")
        elif chon == "0":
            print("Cuts") 
            break
        else:
            print("Lua chon khong hop le")
menu()
'''

def main():
    tong=0
    n = int(input("Nhập số khách VIP: "))
    for i in range(n):
        print(f"\nNhập khách thứ {i+1}:")
        vip = VIPCustomer()
        vip.input()
        tong += vip.thanh_tien()
        ds_khach.append(vip)
    print("\n--- DANH SACH KHACH VIP ---")
    for i, kh in enumerate(ds_khach, 1):
        print(f"\nKhach hang {i}: ")
        kh.output()
    print(f"tong doanh thu {tong}")
main()