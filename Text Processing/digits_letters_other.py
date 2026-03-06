input_data = input()
digits = ''
characters = ''
others = ''

for char in input_data:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        characters += char
    else:
        others += char

print(digits)
print(characters)
print(others)