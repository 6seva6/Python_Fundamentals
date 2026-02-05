input_numbers = list(map(int, input().split(", ")))
sorted_number_indices = [i for i in range(len(input_numbers)) if input_numbers[i] % 2 == 0]
print(sorted_number_indices)