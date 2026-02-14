initial_energy = float(input())
artefact_counter = 0
mountine_counter = 0

while True:
    command = input()

    if command == "Journey ends here!":
        if artefact_counter == 3:
            print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
        else:
            print(f"The character could not find all the pieces and needs {3 - artefact_counter} more to complete the legendary artifact.")
        break

    elif command == "mountain":
        mountine_counter += 1
        initial_energy -= 10
        if mountine_counter %3 == 0:
            artefact_counter += 1
        if artefact_counter == 3:
            print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
            break

    elif command == "desert":
        initial_energy -= 15

    elif command == "forest":
        initial_energy += 7

    if initial_energy <= 0:
        print(f"The character is too exhausted to carry on with the journey.")
        break