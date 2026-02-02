counter = 0
while True:
    string = str(input())
    if string == 'END':
        break
    elif string == 'cat' or string == 'dog' or string == 'coding' or string == 'movie':
        counter += 1
    elif string == 'CAT' or string == 'DOG' or string == 'CODING' or string == 'MOVIE':
        counter += 2
    else:
        continue
if counter < 5:
    print(counter)
else:
    print('You need extra sleep')
