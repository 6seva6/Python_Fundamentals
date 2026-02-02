input_gifts = input().split()
command = input().split()
while command[0] + command[1] != "NoMoney":
    if command[0] == "OutOfStock" and command[1] in input_gifts:
        for i in range(len(input_gifts)):
            if input_gifts[i] == command[1]:
                input_gifts[i] = "None"
    elif command[0] == "Required" and 0 <= int(command[2]) <= len(input_gifts):
        input_gifts[int(command[2])] = command[1]
    elif command[0] == "JustInCase":
        input_gifts[-1] = command[1]
    command = input().split()

for j in range(len(input_gifts)):
    if input_gifts[j] == "None":
        continue
    else:
        print(f"{input_gifts[j]}", end = " ")