import re

raw_line = input()
raw_result = ''
while raw_line != 'Purchase':
    raw_result += raw_line
    raw_line = input()

pattern = r'>>(\w+)<<([0-9]+\.?[0-9]*)!(\d+)'
total_money_spend = 0
bought_furniture = []

results = re.finditer(pattern, raw_result)

for match in results:
    bought_furniture.append(match.group(1))
    total_money_spend += float(match.group(2))*int(match.group(3))

print('Bought furniture:')
for i in bought_furniture:
    print(i)

print(f'Total money spend: {total_money_spend:.2f}')
