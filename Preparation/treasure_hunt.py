def treasure_hunt(command_, initial_loot_):
    if command_[0] == "Loot":
        for loot in command_[1::]:
            if loot not in initial_loot_:
                initial_loot_.insert(0, loot)
        return  initial_loot_ , None
    elif command_[0] == "Drop":
        if not 0 <= int(command_[1]) <= len(initial_loot_):
            return initial_loot_ , None
        else:
            removed_loot = initial_loot_.pop(int(command_[1]))
            initial_loot_.append(removed_loot)
            return initial_loot_ , None
    elif command_[0] == "Steal":
        if len(initial_loot_) <= int(command_[1]):
            return None, initial_loot_
        else:
            left_loot =  initial_loot_[:len(initial_loot_) - int(command_[1])]
            return left_loot , initial_loot_[len(initial_loot_) - int(command_[1]):]
    return None,None

initial_loot = [loot for loot in input().split("|")]
command = []

while True:
    command = input().split()
    if command[0] == "Yohoho!":
        sum_gain = 0
        for num in initial_loot:
            sum_gain += len(num)
        average_gain = sum_gain / len(initial_loot)
        print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
        break
    initial_loot, stolen_loot = treasure_hunt(command, initial_loot)
    if stolen_loot:
        print(", ".join(stolen_loot))
    if not initial_loot:
        print(f"Failed treasure hunt.")
        break