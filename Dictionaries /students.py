all_students = {}
course = ""

while True:
    command = input()
    if ":" not in command:
        course = command
        break
    else:
        command = command.split(":")
        key = command[0]
        value = command[1::]
        all_students[key] = value

if "_" in course:
    temp_course = course.replace("_", " ")
    course = temp_course

for key, value in all_students.items():
    if course in value:
        print(f"{key} - {value[0]}")