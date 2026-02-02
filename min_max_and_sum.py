input_numbers = input().split()

def min_max(input_list):
    for i in range(len(input_list)):
        input_list[i] = int(input_list[i])
    min_value = min(input_list)
    max_value = max(input_list)
    sum_value = sum(input_list)
    return min_value, max_value, sum_value

minimum_number, maximum_number, sum_numbers = min_max(input_numbers)
print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_numbers}")