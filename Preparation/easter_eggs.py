import re

data_egs = input()

pattern = r'[@#]+([a-z]{3,})[@#]+[^A-Za-z0-9]*[/]+(\d+)[/]+'

matches = re.finditer(pattern, data_egs)

for match in matches:
    print(f'You found {match.group(2)} {match.group(1)} eggs!')