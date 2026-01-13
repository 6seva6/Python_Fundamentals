number_quantity=int(input())

for i in range(number_quantity):
    number = int(input())
    if number % 2 != 0:
        print(f'{number} is odd!')
        break
else:
    print('All numbers are even.')
