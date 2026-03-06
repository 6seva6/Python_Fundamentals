input_data = input().split()
processed_data = [value * len(value) for value in input_data]

print(''.join(processed_data))