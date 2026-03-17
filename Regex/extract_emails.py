import re

raw_string = input()

pattern = r'([a-zA-Z0-9._,-]+)@([A-Za-z-]+\.){1,}[A-Za-z]{1,}'

result = re.finditer(pattern, raw_string)

for match in result:
    print(match.group())