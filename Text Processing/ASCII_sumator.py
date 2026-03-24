start_range = ord(input())
end_range = ord(input())

string = input()
list_ascii_values = [ord(value) for value in string]
summ = 0

for value in list_ascii_values:
    if start_range < value < end_range:
        summ += value

print(summ)