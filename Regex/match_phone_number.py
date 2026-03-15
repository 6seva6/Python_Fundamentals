import re

numbers = input()

template = r"(\+359)([ -])2\2\d{3}\2\d{4}\b"

result = re.finditer(template, numbers)
numbers = []

for match in result:
    numbers.append(match.group())

print(", ".join(numbers))