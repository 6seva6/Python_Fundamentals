integer_sequence = [int(number) for number in input().split()]
avg_value = sum(integer_sequence)/len(integer_sequence)
all_value = list(sorted(filter(lambda x: x > avg_value, integer_sequence), reverse=True))
sorted_value = [all_value[value] for value in range(len(all_value)) if value <= 4]
if not sorted_value:
    print(f"No")
else:
    print(" ".join(str(x) for x in sorted_value))
