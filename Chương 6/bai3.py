_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = [x for x in _list if x % 2 == 0]
odd_list = [x for x in _list if x % 2 != 0]

print(f"List số chẵn (even): {even_list}")
print(f"List số lẻ (odd): {odd_list}")