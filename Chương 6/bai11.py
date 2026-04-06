n = int(input("Nhập độ dài n: "))
_list = ['apple', 'banana', 'kiwi', 'orange', 'pie']

_new = [word for word in _list if len(word) > n]
print(f"Các từ có độ dài lớn hơn {n}: {_new}")