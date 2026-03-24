import re

pattern = r'w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+'

raw_text = ''

while (raw_input:= input())!= '':
    raw_text += raw_input

match = re.finditer(pattern, raw_text)

for link in match:
    print(link.group())