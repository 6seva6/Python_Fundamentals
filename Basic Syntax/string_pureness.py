number_of_strings = int(input())

for i in range(number_of_strings):
    string = str(input())
    if ',' in string or '.' in string or '_' in string:
        print(f'{string} is not pure.')
    else:
        print(f'{string} is pure.')