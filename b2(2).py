'''
Tạo 1 lớp Học sinh: Họ tên, ngày sinh, Diem toán, điểm văn
Phương thức: Hàm tạo rỗng, input, output
Tạo lớp Học sinh chuyên văn kế thừa lớp học sinh có thuộc tính: Lớp
Phương thức: Hàm tạo, input, output, diemTB=(Văn*2+toán)/3
Xếp loại: ĐTB<5=> Kém; ĐTB<6.5=>TB; ĐTB<7.5 -> KHá; DTB<9-> giỏi còn lại là xuất sắc
Luồng main: 1. Nhập danh sách học sinh chuyên văn
            2. Thêm một học sinh bất kỳ
            3. Ghi danh sách học sinh lên 1 tệp bất kỳ
Đọc nội dung tệp vừa ghi ở trên và thực hiện các chức năng:
    1. Đưa ra các sinh viên viên được xếp loại xuất sắc
    2. Đưa ra sinh viên có điểm trung bình thấp nhất
'''
import pickle

class Hocsinh:
    def __init__(self):
        self.Hoten = " "
        self.Ngaysinh = " "
        self.Diemtoan = 0.0
        self.Diemvan = 0.0

    def input(self):
        self.Hoten = input("Nhập họ tên: ")
        self.Ngaysinh = input("Nhập ngày sinh: ")
        self.Diemtoan = float(input("Nhập điểm Toán: "))
        self.Diemvan = float(input("Nhập điểm Văn: "))

    def output(self):
        print("Họ tên:", self.Hoten)
        print("Ngày sinh:", self.Ngaysinh)
        print("Điểm Toán:", self.Diemtoan)
        print("Điểm Văn:", self.Diemvan)


class HS_ChuyenVan(Hocsinh):
    def __init__(self):
        super().__init__()
        self.Lop = " "

    def input(self):
        super().input()
        self.Lop = input("Nhập lớp: ")

    def output(self):
        super().output()
        print("Lớp:", self.Lop)
        print("Điểm TB:", self.DiemTB())
        print("Xếp loại:", self.Xeploai())

    def DiemTB(self):
        return (self.Diemvan * 2 + self.Diemtoan) / 3

    def Xeploai(self):
        dtb = self.DiemTB()
        if dtb < 5:
            return "Kém"
        elif dtb < 6.5:
            return "Trung bình"
        elif dtb < 7.5:
            return "Khá"
        elif dtb < 9:
            return "Giỏi"
        else:
            return "Xuất sắc"


def main():
    ds = []

    # 1. Nhập danh sách học sinh chuyên văn
    n = int(input("Nhập số lượng học sinh chuyên văn: "))
    for i in range(n):
        print(f"\nNhập thông tin học sinh thứ {i + 1}")
        hs = HS_ChuyenVan()
        hs.input()
        ds.append(hs)

    # 2. Thêm một học sinh bất kỳ
    print("\nNhập thông tin học sinh thêm:")
    hs_moi = HS_ChuyenVan()
    hs_moi.input()
    ds.append(hs_moi)

    # 3. Ghi danh sách học sinh vào file
    with open("ds_hs.dat", "wb") as f:
        pickle.dump(ds, f)
    print("\nĐã ghi danh sách vào tệp 'ds_hs.dat'")

    # Đọc lại danh sách từ file
    with open("ds_hs.dat", "rb") as f:
        ds_tu_file = pickle.load(f)

    # 1. Đưa ra các sinh viên xếp loại xuất sắc
    print("\nDanh sách học sinh xếp loại Xuất sắc:")
    for hs in ds_tu_file:
        if hs.Xeploai() == "Xuất sắc":
            hs.output()
            print("-" * 30)

    # 2. Đưa ra sinh viên có điểm trung bình thấp nhất
    if ds_tu_file:
        hs_min = min(ds_tu_file, key=lambda hs: hs.DiemTB())
        print("\nHọc sinh có điểm trung bình thấp nhất:")
        hs_min.output()


if __name__ == "__main__":
    main()
