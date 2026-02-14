def playlist(command_, starting_list_):
    if command_[0] == "Add Song":
        if command[1] in starting_list_:
            return starting_list_, None
        else:
            starting_list_.append(command[1])
            return starting_list_, f"{command[1]} successfully added"
    elif command_[0] == "Delete Song":
        if int(command[1]) < len(starting_list_):
            deleted_songs = starting_list_[:int(command[1])]
            starting_list_ = starting_list_[int(command[1])::]
            return starting_list_, f"{', '.join(deleted_songs)} deleted"
        else:
            return starting_list_, None

    elif command_[0] == "Shuffle Songs":
        if 0 <= int(command[1]) < len(starting_list_) and 0 <= int(command[2]) < len(starting_list_):
            temp = starting_list_[int(command_[1])]
            starting_list_[int(command_[1])] = starting_list_[int(command[2])]
            starting_list_[int(command[2])] = temp
            return starting_list_, f"{starting_list_[int(command_[1])]} is swapped with {starting_list_[int(command[2])]}"
        else:
            return starting_list_, None

    elif command_[0] == "Insert":
        if 0 <= int(command[2]) < len(starting_list_):
            if command_[1] in starting_list_:
                return starting_list_, f"Song is already in the playlist"
            else:
                starting_list_.insert(int(command[2]), command_[1])
                return starting_list_, f"{command_[1]} successfully inserted"
        else:
            return starting_list_, f"Index out of range"

    elif command_[0] == "Sort":
        starting_list_ = sorted(starting_list_, reverse=True)
        return starting_list_, None

    elif command_[0] == "Play":
        return starting_list_, "Songs to Play:\n" + "\n".join(starting_list_)

    return None, None

starting_lis = input().split()
number_of_commands = int(input())

for i in range(number_of_commands):
    command = input().split(" * ")
    starting_lis, message = playlist(command, starting_lis)
    if message:
        print(message)