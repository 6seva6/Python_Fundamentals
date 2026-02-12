initial_health = 100
initial_bitcoins = 0
rooms = [item for item in input().split("|")]
is_dead = False
counter = 0

health = initial_health
for command in rooms:
    counter += 1
    if command.split()[0] == "potion":
        value = int(command.split()[1])
        current_health = health
        health += value
        if health > 100:
            value = 100 - current_health
            health = 100
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")
    elif command.split()[0] == "chest":
        value = int(command.split()[1])
        initial_bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= int(command.split()[1])
        if health <= 0 :
            print(f"You died! Killed by {command.split()[0]}.")
            print(f"Best room: {counter}")
            is_dead = True
            break
        print(f"You slayed {command.split()[0]}.")

if not is_dead:
    print(f"You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {health}")