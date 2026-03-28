import time
x = time.localtime()
year = x[0]
nam_sinh = int(input("Nhập vào năm sinh: "))

tuoi = year - nam_sinh
print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")
