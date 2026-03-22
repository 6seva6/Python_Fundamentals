import re

raw_input = input()

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

all_food_items = re.findall(pattern, raw_input)

kcal = 0

for item in all_food_items:
    kcal+= int(item[3])

days_left = int(kcal/2000)

print(f'You have food to last you for: {days_left} days!')

if days_left > 0:
    for item in all_food_items:
        print(f'Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}')