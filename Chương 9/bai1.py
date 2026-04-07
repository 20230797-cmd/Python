# a) Tạo class hoc_vien với các thuộc tính tương ứng
class hoc_vien:
    def __init__(self, ho_ten, ngay_sinh, email, dien_thoai, dia_chi, lop):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.email = email
        self.dien_thoai = dien_thoai
        self.dia_chi = dia_chi
        self.lop = lop

    # b) Tạo phương thức show_info trả về đầy đủ thông tin
    def show_info(self):
        print("THÔNG TIN HỌC VIÊN")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Ngày sinh: {self.ngay_sinh}")
        print(f"Email: {self.email}")
        print(f"Điện thoại: {self.dien_thoai}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Lớp: {self.lop}")

    # c) Tạo phương thức change_info với tham số mặc định
    def change_info(self, dia_chi='Hà Nội', lop='IT12.x'):
        self.dia_chi = dia_chi
        self.lop = lop
        print(f"Đã cập nhật Địa chỉ mới: {dia_chi} và Lớp mới: {lop} ")

# d) Chương trình chính
# Tạo đối tượng học viên
hv1 = hoc_vien("Nguyễn Thành Đạt", "24/06/2005", "kp2462005@gmail.com", "0965401528", "Uông Bí", "IT14.2")

hv1.show_info()
hv1.change_info()
hv1.show_info()