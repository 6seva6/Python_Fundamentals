import re

dates = input()
pattern = r'\b(\d{2})([.\-/])([A-Z][a-z]{2})\2(\d{4})\b'
result = re.finditer(pattern, dates)

for match in result:
    print(f'Day: {match.group(1)}, Month: {match.group(3)}, Year: {match.group(4)}')