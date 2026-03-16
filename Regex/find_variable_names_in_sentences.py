import re

raw_string = input()

pattern = r'(?<=_)[a-zA-Z0-9]+'

result = re.findall(pattern, raw_string)

print(','.join(result))