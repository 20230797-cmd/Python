# Sinh viên: Phạm Gia Khánh - MSSV: 20230797 - Lớp: DCCNTT14.2

# 1. Hàm tính tổng 2 số
def tinh_tong_2_so(a, b):
    return a + b

# 2. Hàm tính tổng các số truyền vào
def tinh_tong_nhieu_so(*args):
    return sum(args)

# 3. Hàm kiểm tra một số nguyên tố
def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Hàm tìm các số nguyên tố trong khoảng [a,b]
def tim_nguyen_to_khoang(a, b):
    ket_qua = []
    for i in range(a, b + 1):
        if kiem_tra_nguyen_to(i):
            ket_qua.append(i)
    return ket_qua

# 5. Hàm kiểm tra số hoàn hảo 
def kiem_tra_hoan_hao(n):
    if n < 2:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

# 6. Hàm tìm các số hoàn hảo trong khoảng [a,b]
def tim_hoan_hao_khoang(a, b):
    ket_qua = []
    for i in range(a, b + 1):
        if kiem_tra_hoan_hao(i):
            ket_qua.append(i)
    return ket_qua
def chuong_trinh_menu():
    while True:
        print("\n" + "="*40)
        print("MENU CHỌN CHỨC NĂNG")
        print("="*40)
        print("1. Tính tổng 2 số")
        print("2. Tính tổng nhiều số")
        print("3. Kiểm tra một số nguyên tố")
        print("4. Tìm các số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra một số hoàn hảo")
        print("6. Tìm các số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát chương trình")
        
        chon = input("Nhập lựa chọn của bạn (0-6): ")
        
        if chon == '1':
            a = float(input("Nhập số thứ nhất: "))
            b = float(input("Nhập số thứ hai: "))
            print(f"=> Tổng 2 số là: {tinh_tong_2_so(a, b)}")
            
        elif chon == '2':
            nhap = input("Nhập các số, cách nhau bởi dấu cách (VD: 1 2.5 3 4): ")
            # Chuyển chuỗi nhập vào thành danh sách các số thực
            danh_sach_so = [float(x) for x in nhap.split()]
            print(f"=> Tổng các số là: {tinh_tong_nhieu_so(*danh_sach_so)}")
            
        elif chon == '3':
            n = int(input("Nhập số nguyên dương cần kiểm tra: "))
            if kiem_tra_nguyen_to(n):
                print(f"=> {n} là số nguyên tố.")
            else:
                print(f"=> {n} không là số nguyên tố.")
                
        elif chon == '4':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print(f"=> Các số nguyên tố trong khoảng [{a}, {b}] là: {tim_nguyen_to_khoang(a, b)}")
            
        elif chon == '5':
            n = int(input("Nhập số nguyên dương cần kiểm tra: "))
            if kiem_tra_hoan_hao(n):
                print(f"=> {n} số hoàn hảo.")
            else:
                print(f"=> {n} không là số hoàn hảo.")
                
        elif chon == '6':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print(f"=> Các số hoàn hảo trong khoảng [{a}, {b}] là: {tim_hoan_hao_khoang(a, b)}")
            
        elif chon == '0':
            print("Đã thoát chương trình")
            break
            
        else:
            print("Lựa chọn không hợp lệ")

# Chạy chương trình
if __name__ == "__main__":
    chuong_trinh_menu()
