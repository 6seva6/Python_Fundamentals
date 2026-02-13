initial_energy = int(input())
wins = 0
while True:
    distance_to_enemy = input()
    if distance_to_enemy == "End of battle":
        print(f"Won battles: {wins}. Energy left: {initial_energy}")
        break
    elif initial_energy - int(distance_to_enemy) < 0:
        print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
        break
    initial_energy -= int(distance_to_enemy)
    wins += 1
    if wins % 3 ==0:
        initial_energy += wins