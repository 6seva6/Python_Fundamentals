def robo_journey(command_, grid_,robo_items_):

    if command_[0] == "Step Backward":
        start = int(command_[1])
        steps = int(command_[2])
        if 0 <= start < len(grid_):
            end =(start - steps) % len(grid_)
            robo_items_ += grid_[end]
            grid_[end] = 0
            return grid_, robo_items_
        else:
            return grid_, robo_items_
    elif command_[0] == "Step Forward":
        start = int(command_[1])
        steps = int(command_[2])
        if 0 <= start < len(grid_):
            end = (start + steps) % len(grid_)
            robo_items_ += grid_[end]
            grid_[end] = 0
            return grid_, robo_items_
        else:
            return grid_, robo_items_

    elif command_[0] == "Double":
        if 0 <= int(command_[1]) < len(grid_):
            grid_[int(command_[1])] *= 2
            return grid_, robo_items_
        else:
            return grid_, robo_items_

    elif command_[0] == "Switch":
        grid_ = grid_[::-1]
        return grid_, robo_items_

    return grid_, robo_items_

grid = [int(x) for x in input().split("|")]
robo_items = 0

while True:
    command = input()
    if command.startswith("Double"):
        command = command.split()
    else:
        command = command.split("$")
    if command[0] == "Adventure over":
        print(" - ".join(str(x) for x in grid))
        print(f"Robo finished the adventure with {robo_items} items!")
        break
    grid, robo_items = robo_journey(command, grid, robo_items)
