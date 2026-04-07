class hoc_vien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    def show_info(self):
        print(f"\n--- THÔNG TIN: {self.ho_ten.upper()} ---")
        print(f"Ngày sinh: {self.ngay_sinh}")
        print(f"Email: {self.email}")
        print(f"Điện thoại: {self.dien_thoai}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Lớp: {self.lop}")

    def change_info(self, dia_chi='Hà Nội', lop='IT12.x'):
        self.dia_chi = dia_chi
        self.lop = lop
        print(f"Đã cập nhật thông tin cho {self.ho_ten}")

hv1 = hoc_vien("Phạm Gia Khánh", "21/01/2005", "vana@email.com", "0987887654", "Hà Nội", "IT14.2")

hv1.show_info()
hv1.change_info() 
hv1.show_info()
hv1.change_info(dia_chi='Cần Thơ', lop='IT_PRO')
hv1.show_info()

print(f"\nKiểm tra nhanh Email: {hv1.email}")