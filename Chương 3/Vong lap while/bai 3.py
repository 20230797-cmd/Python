n = int(input("Nhập vào số nguyên dương n = "))

if n < 2:
    print("Không phải số nguyên tố.")
else:
    la_nguyen_to = True
    i = 2

    while i < n:
        if n % i == 0:
            la_nguyen_to = False
            break # Thoát vòng lặp ngay nếu thấy chia hết
        i += 1
        
    if la_nguyen_to == True:
        print("Đây là số nguyên tố.")
    else:
        print("Không phải số nguyên tố.")
