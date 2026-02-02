string_numbers = input().split()
int_numbers = []
for number in string_numbers:
    int_numbers.append(int(number))

print(sorted(int_numbers))