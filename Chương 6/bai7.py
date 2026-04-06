_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']
_new1 = [x for x in _list if _list.count(x) == 1]
print(f"Loại bỏ tất cả các phần tử trùng: {_new1}")
_new2 = []
for x in _list:
    if x not in _new2:
        _new2.append(x)
print(f"Chỉ giữ lại 1 phần tử đại diện: {_new2}")