number_of_students = int(input())
total_number_of_lectures = int(input())
additional_bonus = int(input())

count_of_attendances = [int(input()) for _ in range(number_of_students)]

max_attendance = max(count_of_attendances) if count_of_attendances else 0

total_bonus = 0
if total_number_of_lectures > 0:
    total_bonus = max_attendance / total_number_of_lectures * (5 + additional_bonus)

print(f"Max Bonus: {round(total_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")