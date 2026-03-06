first_string = input()
second_string = input()

while first_string in second_string:
    new_string = second_string.replace(first_string, '')
    second_string = new_string
print(second_string)