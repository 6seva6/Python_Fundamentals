input_score = list(map(int, input().split()))
happines_factor = int(input())
multiplied_values = [x * happines_factor for x in input_score]
avg_multiplied_values = sum(multiplied_values) / len(input_score)
happy_employee = sum(num >= avg_multiplied_values for num in multiplied_values)

if happy_employee < len(input_score)/2:
    print(f"Score: {happy_employee}/{len(input_score)}. Employees are not happy!")
else:
    print(f"Score: {happy_employee}/{len(input_score)}. Employees are happy!")