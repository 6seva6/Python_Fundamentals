number_of_electrons = int(input())

def electron_shell_list(electrons):
    """
    Fill the electron shell list with given number of electrons.
    :param electrons:
    :return: shells with number of electrons
    """
    list = []
    counter = 1
    electrons_left = electrons
    while True:
        if 2*(counter**2) > electrons_left:
            if counter > 1 and electrons_left > 0:
                list.append(electrons_left)
            break
        else:
            list.append(2*(counter**2))
            electrons_left -= 2*(counter**2)
            counter += 1
    return list

answer = electron_shell_list(number_of_electrons)
print(answer)