import re

raw_string = input()
list_raw_string = []
while raw_string != '':
    list_raw_string.append(raw_string)
    raw_string = input()

raw_string = ' '.join(list_raw_string)
pattern = r'\d+'

result = re.findall(pattern, raw_string)

print(' '.join(result))
