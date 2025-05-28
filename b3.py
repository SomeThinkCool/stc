'''
Câu 3: Cơ sở dữ liệu Quản lý sinh viên (QL.Sinhvien)
Tạo cơ sở dữ liệu gồm 2 bảng:
    - Lop (Malop, Tenlop, Siso)
    - Sinhvien (Masv, Hoten, Ngaysinh, Malop, DiemTB)
Yêu cầu:
    - Nhập mỗi bảng 5 bản ghi.
    - In danh sách sinh viên gồm: Masv, Hoten, Tenlop, DiemTB và phân loại học lực theo điều kiện:
        + Giỏi: DiemTB >= 8
        + Khá: 6.5 <= DiemTB < 8
        + Trung bình: 5 <= DiemTB < 6.5
        + Yếu: DiemTB < 5
'''

import sqlite3
conn = sqlite3.connect("QLSV.db")
cursor = conn.cursor()
cursor.execute("""
            CREATE TABLE IF NOT EXISTS Lop(
               Malop TEXT PRIMARY KEY,
               Tenlop TEXT,
               Siso INTEGER
               )""")
cursor.execute("""
            CREATE TABLE IF NOT EXISTS Sinhvien(
               Masv TEXT PRIMARY KEY,
               Hoten TEXT,
               Ngaysinh TEXT,
               Malop TEXT,
               DiemTB FLOAT,
               FOREIGN KEY (Malop) REFERENCES Lop(Malop)
               )""")

lop = [
    ("L01", "CNTT", 30),
    ("L02", "QTKD", 31),
    ("L03", "NNA", 34),
    ("L04", "DL", 24),
    ("L05", "DTTT", 16),
]
cursor.executemany("INSERT INTO Lop VALUES (?,?,?)", lop)
sinhvien = [
    ("SV01", "A", "20/1/2000", "L01", 9),
    ("SV02", "B", "20/2/2000", "L02", 8),
    ("SV03", "C", "20/3/2005", "L03", 4),
    ("SV04", "D", "20/4/2004", "L04", 6),
    ("SV05", "E", "20/5/2000", "L05", 7),
]
cursor.executemany("INSERT INTO Sinhvien VALUES (?,?,?,?,?)", sinhvien)
query = """
SELECT sv.Masv AS "Ma sinh vien",
       sv.Hoten AS "Ho ten",
       l.Tenlop AS "Ten lop",
       sv.DiemTB AS "Diem TB",
       CASE 
          WHEN sv.DiemTB >= 8 THEN 'Giỏi'
          WHEN sv.DiemTB >= 6.5 THEN 'Khá'
          WHEN sv.DiemTB >= 5 THEN 'Trung bình'
          ELSE 'Yếu'
       END AS "Hoc luc"
FROM Sinhvien sv
JOIN Lop l ON sv.Malop=l.Malop
"""
cursor.execute(query)
rows = cursor.fetchall()
col1=15
col2=15
col3=15
col4=15
col5=15

tieude = f" | {'Ma sinh vien':<{col1}} | {'Ho ten':<{col2}} | {'Ten lop':<{col3}} | {'Diem TB':<{col4}} | {'Hoc luc':<{col5}} |"
dorong = f" | {'-' * col1}-|-{'-' * col2}-|-{'-' * col3}-|-{'-' * col4}-|-{'-' * col5} |"
print(tieude)
print(dorong)
for Masv, Hoten, Malop, DiemTB, Hocluc in rows:
    print( f" | {Masv:<{col1}} | {Hoten:<{col2}} | {Malop:<{col3}} | {DiemTB:<{col4}} | {Hocluc:<{col5}} |")
conn.close()