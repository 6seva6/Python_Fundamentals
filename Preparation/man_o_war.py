pirate_ship = [int(ship) for ship in input().split(">")]
war_ship = [int(ship) for ship in input().split(">")]
max_health_capacity = int(input())
sunk = False


def is_sink(command_,stalemate):

    if command_[0] == "Fire":
        if not 0<= int(command_[1]) < len(war_ship):
            return None, stalemate

        war_ship[int(command_[1])] -= int(command_[2])
        if war_ship[int(command_[1])] <= 0:
            return "You won! The enemy ship has sunken.", True

    elif command_[0] == "Defend":
        if not 0 <= int(command_[1]) <= int(command_[2]) < len(pirate_ship) :
            return None, stalemate

        for section in range(int(command_[1]), int(command_[2])+1):
            pirate_ship[section] -= int(command_[3])
            if pirate_ship[section] <= 0:
                return "You lost! The pirate ship has sunken.", True

    elif command_[0] == "Repair":
        if not 0 <= int(command_[1]) < len(pirate_ship):
            return None, stalemate

        pirate_ship[int(command_[1])] += int(command_[2])
        if pirate_ship[int(command_[1])] > max_health_capacity:
            pirate_ship[int(command_[1])] = max_health_capacity

    elif command_[0] == "Status":
        repair = sum(1 for section in pirate_ship if section < max_health_capacity * 0.2)
        return f"{repair} sections need repair.", stalemate

    return None, sunk

while True:
    command = [value for value in input().split()]
    if command[0] == "Retire":
        break
    answer, sunk = is_sink(command, sunk)
    if answer:
        print(answer)
    if sunk:
        break

if not sunk:
    pirate_ship_sum = sum(pirate_ship)
    war_ship_sum = sum(war_ship)
    print(f"Pirate ship status: {pirate_ship_sum}")
    print(f"Warship status: {war_ship_sum}")