def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhập danh sách các từ, cách nhau bởi dấu phẩy: ")
numbers = [int(num) for num in input_list.split(',')]
lst_dao_nguoc = dao_nguoc_list(numbers)
print(f"Danh sách đảo ngược là: {lst_dao_nguoc}")