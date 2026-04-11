import math_utils

p1 = (1, 2)
p2 = (3, 4)

tong = math_utils.phanso.cong(p1, p2)
hieu = math_utils.phanso.tru(p1, p2)
tich = math_utils.phanso.nhan(p1, p2)
thuong = math_utils.phanso.chia(p1, p2)

print(f"Phan so 1: {p1[0]}/{p1[1]}")
print(f"Phan so 2: {p2[0]}/{p2[1]}")
print(f"Tong: {tong[0]}/{tong[1]}")
print(f"Hieu: {hieu[0]}/{hieu[1]}")
print(f"Tich: {tich[0]}/{tich[1]}")
print(f"Thuong: {thuong[0]}/{thuong[1]}")
print("-" * 20)

bk = 5
print(f"Hinh tron ban kinh = {bk}")
print(f"Chu vi: {math_utils.hinhhoc.chu_vi_hinh_tron(bk)}")
print(f"Dien tich: {math_utils.hinhhoc.dien_tich_hinh_tron(bk)}")
print("-" * 20)

cd = 4
cr = 3
print(f"Hinh chu nhat ({cd}x{cr})")
print(f"Chu vi: {math_utils.hinhhoc.chu_vi_hinh_chu_nhat(cd, cr)}")
print(f"Dien tich: {math_utils.hinhhoc.dien_tich_hinh_chu_nhat(cd, cr)}")