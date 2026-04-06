
_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']
do_dai_min = 4
count = 0

for s in _list:
    if len(s) >= do_dai_min and s[0] == s[-1]:
        count += 1

print(f"Số lượng chuỗi thỏa mãn điều kiện: {count}")