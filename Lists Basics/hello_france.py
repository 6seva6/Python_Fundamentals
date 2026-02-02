input_items = input().split("|")
buget = int(input())
float_values = []
valid_values = []

for price in range(len(input_items)):
    start_index = input_items[price].index(">")
    float_values.append(float(input_items[price] [start_index+1::]))

float_values_index = 0
for item in input_items:
    if "Clothes" in item and float_values[float_values_index] < 50.00:
        valid_values.append(float_values[float_values_index])
    elif "Shoes" in item and float_values[float_values_index] < 35.00:
        valid_values.append(float_values[float_values_index])
    elif "Accessories" in item and float_values[float_values_index] < 20.50:
        valid_values.append(float_values[float_values_index])
    float_values_index += 1
total_sellins = 0
buget_left = buget

for item in range(len(valid_values)):
    if buget_left - valid_values[item] < 0:
        continue
    else:
        buget_left -= valid_values[item]
        sell_price = valid_values[item] + (valid_values[item] * 0.4)
        total_sellins += sell_price
        print(f"{sell_price:.2f}", end=" ")

profit = (total_sellins - buget) + buget_left
print()
print(f"Profit: {profit:.2f}")

if profit + buget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")