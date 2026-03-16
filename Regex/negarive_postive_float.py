import re

raw_text = input()

pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?(?=\s)'

result = re.finditer(pattern, raw_text)

filtered_result = [match.group() for match in result]

print(' '.join(filtered_result))