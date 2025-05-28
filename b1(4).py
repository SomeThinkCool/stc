'''
- Tong le/chan giua a,b
- S = 1.2+2.3+3.4+...+n(n+1)
- Tong binh phuong cac so tu x -> y
'''

# Tong chan/le giua a,b
def Tong_chanle(a,b):
    tongchan=0
    tongle=0
    for i in range (a+1,b):
        if i%2==0:
            tongchan+=i
        else: tongle+=i
    print("Tong chan: ",tongchan)
    print("Tong le: ",tongle)
    print("Tong cac so tu a -> b: ",tongle+tongchan)

# a=int(input("Nhap so a: "))
# b=int(input("Nhap so b: "))
# Tong_chanle(a,b)

# S = 1.2+2.3+3.4+...+n(n+1)

# Tong binh phuong cac so tu x -> y

def tim_cac_cap(danh_sach, S):
    """
    Tìm tất cả các cặp (a, b) trong danh sách sao cho a + b = S.

    Args:
        danh_sach: Danh sách số nguyên.
        S: Số nguyên cần tìm tổng.

    Returns:
        Danh sách các cặp (a, b) thỏa mãn điều kiện.
    """

    cac_cap = []
    # Sử dụng vòng lặp for để duyệt qua từng phần tử trong danh sách
    for i in range(len(danh_sach)):
        # Lấy phần tử thứ i
        a = danh_sach[i]
        # Tính phần tử b cần tìm
        b = S - a
        # Duyệt qua danh sách để tìm phần tử b
        for j in range(len(danh_sach)):
            if danh_sach[j] == b and i != j:  # Tránh trường hợp a và b trùng nhau
                cac_cap.append((a, b))
                break  # Tìm được b thì thoát khỏi vòng lặp trong

    return cac_cap

# Ví dụ
danh_sach = [1, 2, 3, 4, 5]
S = 7
cac_cap = tim_cac_cap(danh_sach, S)
print(f"Các cặp (a, b) sao cho a + b = {S} là: {cac_cap}") # Output: [(2, 5), (3, 4)]

danh_sach = [1, 2, 3, 4, 5]
S = 6
cac_cap = tim_cac_cap(danh_sach, S)
print(f"Các cặp (a, b) sao cho a + b = {S} là: {cac_cap}") # Output: [(1, 5), (2, 4)]
