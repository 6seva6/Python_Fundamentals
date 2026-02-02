list_numbers = input().split()
int_list = []
for i in list_numbers:
    int_list.append(int(i))

result = filter(lambda number: number % 2 == 0, int_list)
print(list(result))