letters_number = int(input())

for i in range(97, 97+letters_number):
    for j in range(97, 97+letters_number):
        for k in range(97, 97+letters_number):
            print(f'{chr(i)}{chr(j)}{chr(k)}')