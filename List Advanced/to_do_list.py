unsorted_to_do_list = []
while True:
    value = input().split("-")
    if value[0] == 'End':
        break
    unsorted_to_do_list.append(value)

sorted_to_do_list = sorted(unsorted_to_do_list, key=lambda x: int(x[0]))
sorted_to_do_list = [item[1] for item in sorted_to_do_list]

print(sorted_to_do_list)
