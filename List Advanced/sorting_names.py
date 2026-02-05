name_list = [name for name in input().split(", ")]
sorted_name_list = sorted(name_list, key = lambda item: (-len(item),item))
print(sorted_name_list)
