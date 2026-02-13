waiting_people = int(input())
current_lift_state = [int(value) for value in input().split()]


for wagon in range(len(current_lift_state)):
    if current_lift_state[wagon] <= 4:
        added_people = 4 - current_lift_state[wagon]
        if waiting_people < 4:
            added_people = waiting_people
        current_lift_state[wagon] += added_people
        waiting_people -= added_people

if waiting_people == 0 and sum(current_lift_state) < len(current_lift_state) * 4:
    print(f"The lift has empty spots!")
    print(" ".join(str(x) for x in current_lift_state))

elif waiting_people > 0 and sum(current_lift_state) == len(current_lift_state) * 4:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(" ".join(str(x) for x in current_lift_state))

elif waiting_people == 0 and sum(current_lift_state) == len(current_lift_state) * 4:
    print(" ".join(str(x) for x in current_lift_state))