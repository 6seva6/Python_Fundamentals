import re

raw_string = input()
search_string = input()

pattern = re.escape(search_string)

result = re.finditer(pattern, raw_string, re.IGNORECASE)

count = sum(1 for _ in result)

print(count)