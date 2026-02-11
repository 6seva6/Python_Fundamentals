def is_matching(elements_,guess_indexes, counter):
    if (not 0 <= guess_indexes[0] < len(elements_) or
            not 0 <= guess_indexes[1] < len(elements_) or
            guess_indexes[0] == guess_indexes[1]):

        left_side = elements_[:((len(elements_))//2)]
        right_side = elements_[((len(elements_))//2) :]

        center = f"-{counter}a"

        elements_ = [*left_side, center, center, *right_side]
        message_ = f"Invalid input! Adding additional elements to the board"

        return message_, elements_

    elif elements_[guess_indexes[0]] == elements_[guess_indexes[1]]:
        element = elements_[guess_indexes[0]]
        for i in sorted(guess_indexes, reverse=True):
            del elements_[i]
        message_ = f"Congrats! You have found matching elements - {element}!"
        return message_, elements_
    elif elements_[guess_indexes[0]] != elements_[guess_indexes[1]]:
        message_ = f"Try again!"
        return message_, elements_
    return None

sequence_of_elements = [item for item in input().split()]


moves = 0

while True:
    command = [item for item in input().split()]
    if command[0]=="end":
        break
    moves += 1
    indexes = [int(index) for index in command]
    message, sequence_of_elements = is_matching(sequence_of_elements, indexes, moves)
    print(message)
    if not sequence_of_elements:
        print(f"You have won in {moves} turns!")
        break

if sequence_of_elements:
    print(f"Sorry you lose :(")
    print(" ".join(sequence_of_elements))