import re

pattern_name = r'(?<=@)[A-Za-z]+'
pattern_age = r'(?<=#)\d+'

line_number = int(input())

for _ in range(line_number):
    raw_line = input()
    name_match = re.search(pattern_name, raw_line)
    age_match = re.search(pattern_age, raw_line)
    print(f'{name_match.group()} is {age_match.group()} years old.')