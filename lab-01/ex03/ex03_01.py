def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong        
input_list = input("Nhập danh sách các từ, cách nhau bởi dấu phẩy: ")
numbers = [int(num) for num in input_list.split(',')]
tong_chan = tinh_tong_so_chan(numbers)
print(f"Tổng các số chẵn trong danh sách là: {tong_chan}")
