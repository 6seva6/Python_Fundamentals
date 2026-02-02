while True:
    name = str(input())
    counter = 0
    if name == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    for i in name:
        counter += 1
    if counter < 5:
        print(f'{name} goes to Gryffindor.')
    elif counter == 5:
        print(f'{name} goes to Slytherin.')
    elif counter == 6:
        print(f'{name} goes to Ravenclaw.')
    elif counter > 6:
        print(f'{name} goes to Hufflepuff.')