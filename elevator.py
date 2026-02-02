people_number = int(input())
capacity = int(input())
courses = 0


if people_number % capacity == 0:
    courses = int(people_number // capacity)
    print(courses)
elif capacity >= people_number:
    courses = 1
    print(courses)
else:
    courses = int((people_number // capacity) + 1)
    print(courses)

