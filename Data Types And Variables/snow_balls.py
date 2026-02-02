number_of_snowballs = int(input())
value = 0
max_weight = 0
max_time = 0
max_quality = 0
for i in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    new_value = (weight_of_the_snowball // time_needed) ** quality
    if new_value > value:
        value = new_value
        max_weight = weight_of_the_snowball
        max_time = time_needed
        max_quality = quality
print (f'{max_weight} : {max_time} = {value} ({max_quality})')
