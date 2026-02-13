receptionist_1 = int(input())
receptionist_2 = int(input())
receptionist_3 = int(input())
students = int(input())
all_students_per_hour = receptionist_1 + receptionist_2 + receptionist_3
breaks = 0
hours = 0
while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    else:
        students -= all_students_per_hour
print(f"Time needed: {hours}h.")
