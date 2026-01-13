count_number = int(input())

for i in range(count_number):
    value = int(input())
    if value == 88:
        print('Hello')
    elif value == 86:
        print('How are you?')
    elif value < 88:
        print('GREAT!')
    else:
        print('Bye.')