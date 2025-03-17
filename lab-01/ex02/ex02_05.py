so_gio_lam = float(input("Nhập số giờ làm việc hàng tuần của nhân viên: "))
luong_gio = float(input("Nhập mức lương theo giờ chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0,so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Số thực lĩnh của nhân viên là: {thuc_linh}")