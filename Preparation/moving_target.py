def is_target(command_, targets_):
    if command[0] == "Shoot":
        if 0 <= int(command_[1]) < len(targets_):
            targets_[int(command_[1])] -= int(command_[2])
            if targets_[int(command_[1])] <= 0:
                del targets_[int(command_[1])]
        return targets_ , None
    elif command[0] == "Add":
        if 0 <= int(command_[1]) < len(targets_):
            targets_.insert(int(command_[1]), int(command_[2]))
            return targets_ , None
        else:
            return targets_, "Invalid placement!"
    elif command[0] == "Strike":
        if 0 <= int(command_[1])-int(command_[2]) and int(command_[1]) + int(command_[2]) < len(targets_):
            del targets_[int(command_[1])-int(command_[2]): int(command_[1]) + int(command_[2]) + 1]
            return targets_ , None
        else:
            return targets_, "Strike missed!"
    return targets_ , None

targets = [int(target) for target in input().split()]

while True:
    command = input().split()
    if command[0] == "End":
        print("|".join(str(x) for x in targets))
        break
    targets, message = is_target(command, targets)
    if message:
        print(message)