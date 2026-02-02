while True:
    new_string = ''
    string = str(input())
    if string == 'End':
        break
    if string == 'SoftUni':
        continue
    for i in range(len(string)):
        new_string += string[i] + string[i]
    print(new_string)