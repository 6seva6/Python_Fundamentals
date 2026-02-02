tank_capacity = 255
water_pour = 0
number_of_lines = int(input())
for i in range(number_of_lines):
    pour = int(input())
    comparison = 0
    comparison += pour + water_pour
    if pour > tank_capacity:
        print('Insufficient capacity!')
        continue
    elif comparison > tank_capacity:
        print('Insufficient capacity!')
        continue
    else:
        water_pour += pour
print(water_pour)