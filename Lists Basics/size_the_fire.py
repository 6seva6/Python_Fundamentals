fire_sizes = input().split("#")
water = int(input())
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
valid_values = []
effort = 0
total_fire = 0
for size in range(len(fire_sizes)):
    if "High" in fire_sizes[size]:
        current_value = ""
        for i in range(len(fire_sizes[size])):
            if fire_sizes[size][i] in numbers:
                current_value+= fire_sizes[size][i]
        current_value = int(current_value)
        if 81 <= current_value <= 125:
            valid_values.append(current_value)
    elif "Medium" in fire_sizes[size]:
        current_value = ""
        for i in range(len(fire_sizes[size])):
            if fire_sizes[size][i] in numbers:
                current_value+= fire_sizes[size][i]
        current_value = int(current_value)
        if 51 <= current_value <= 80:
            valid_values.append(current_value)
    elif "Low" in fire_sizes[size]:
        current_value = ""
        for i in range(len(fire_sizes[size])):
            if fire_sizes[size][i] in numbers:
                current_value+= fire_sizes[size][i]
        current_value = int(current_value)
        if 1 <= current_value <= 50:
            valid_values.append(current_value)
    else:
        continue

print("Cells:")
for i in range(len(valid_values)):
    if water - valid_values[i] < 0:
        continue
    else:
        print(f" - {valid_values[i]}")
        water = water - valid_values[i]
        effort += valid_values[i]* 0.25
        total_fire += valid_values[i]
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")