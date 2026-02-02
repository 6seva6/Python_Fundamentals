_list = []
for i in range(3):
    _list.append(input())
_list[0], _list[2] = _list[2], _list[0]
print(_list)