'''
Câu 3: Cơ sở dữ liệu quản lý bán hàng (QL.BanHang)
Tạo cơ sở dữ liệu gồm 2 bảng:
    - Sanpham (Masp, Tensp, DonGia)
    - Hoadon (Mahd, Ngaylap, Masp, Soluong)
Yêu cầu:
    - Nhập 5 bản ghi cho mỗi bảng.
    - In danh sách hóa đơn gồm: Mahd, Ngaylap, Tensp, Soluong, DonGia, Thanhtien
Trong đó: Thanhtien = Soluong * DonGia
'''

import sqlite3
conn = sqlite3.connect("QLBH.db")
cursor = conn.cursor()
cursor.execute("""
            CREATE TABLE IF NOT EXISTS Sanpham(
               Masp TEXT PRIMARY KEY,
               Tensp TEXT,
               DonGia FLOAT
               )""")
cursor.execute("""
            CREATE TABLE IF NOT EXISTS Hoadon(
               Mahd TEXT PRIMARY KEY,
               Ngaylap TEXT,
               Masp TEXT,
               Soluong INTEGER,
               FOREIGN KEY (Masp) REFERENCES Sanpham(Masp)
               )""")

sanpham = [
    ("SP01", "Banh", 5000),
    ("SP02", "Keo", 2000),
    ("SP03", "But", 3000),
    ("SP04", "Vo", 10000),
    ("SP05", "Thuoc", 5000),
]
cursor.executemany("INSERT INTO Sanpham VALUES (?,?,?)", sanpham)
hoadon = [
    ("H01", "20/1/2025", "SP01", 9),
    ("H02", "20/2/2025", "SP02", 8),
    ("H03", "20/3/2025", "SP01", 4),
    ("H04", "20/4/2025", "SP04", 6),
    ("H05", "20/5/2025", "SP05", 7),
]
cursor.executemany("INSERT INTO Hoadon VALUES (?,?,?,?)", hoadon)
query = """
SELECT Mahd, Ngaylap, Tensp, Soluong, DonGia, Soluong*Dongia AS Thanhtien
FROM Hoadon hd
JOIN Sanpham sp ON sp.Masp = hd.Masp
"""
cursor.execute(query)
rows = cursor.fetchall()
col1=15
col2=15
col3=15
col4=15
col5=15
col6=15
tieude = f" | {'Ma Hoa don':<{col1}} | {'Ngay lap':<{col2}} | {'Ten san pham':<{col3}} | {'So luong':<{col4}} | {'Don gia':<{col5}} | {'Thanh tien':<{col6}} |"
dorong = f" | {'-' * col1}-|-{'-' * col2}-|-{'-' * col3}-|-{'-' * col4}-|-{'-' * col5}-|-{'-' * col6} |"
print(tieude)
print(dorong)
for Mahoadon, Ngaylap, Tensp, Soluong, Dongia, Thanhtien in rows:
    print( f" | {Mahoadon:<{col1}} | {Ngaylap:<{col2}} | {Tensp:<{col3}} | {Soluong:<{col4}} | {Dongia:<{col5}} | {Thanhtien:<{col6}} |")
conn.close()