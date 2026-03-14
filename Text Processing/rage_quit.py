raw_input = input()

current_string = ''
current_number = ''
result = ''

for char in raw_input:
    if not char.isdigit():
        if current_number:
            result += current_string.upper() * int(current_number)
            current_string = char
            current_number = ''
        else:
            current_string += char

    else:
        current_number += char

if current_string:
    result += current_string.upper() * int(current_number)

unic = len(set(result.upper()))

print(f'Unique symbols used: {unic}')
print(result)