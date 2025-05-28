'''
- Sap xep
'''
#Noi bot
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Hoán đổi

# Ví dụ
# ds = [5, 2, 9, 1, 3]
# bubble_sort(ds)
# print("Dãy sau khi sắp xếp:", ds)
def bubble_sort_giam(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:  # Đảo dấu để giảm dần
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Ví dụ
ds = [5, 2, 9, 1, 3]
bubble_sort_giam(ds)
print("Dãy sau khi sắp xếp giảm dần:", ds)

#Săp xep
def sap_xep_tang(danh_sach):
    return sorted(danh_sach)

# Ví dụ sử dụng
# ds = [5, 2, 9, 1, 3]
# ds_moi = sap_xep_tang(ds)
# print("Dãy sau khi sắp xếp:", ds_moi)

# Chuoi doi xung
def is_palindrome(s):
    # Chuyển chuỗi thành chữ thường và loại bỏ khoảng trắng
    s = s.lower().replace(" ", "")
    # So sánh với chuỗi đảo ngược
    return s == s[::-1]
# Nhập chuỗi từ người dùng
input_string = input("Nhập chuỗi cần kiểm tra: ")
# Gọi hàm và in kết quả
if is_palindrome(input_string):
    print("Chuỗi là chuỗi đối xứng.")
else:
    print("Chuỗi không phải là chuỗi đối xứng.")
