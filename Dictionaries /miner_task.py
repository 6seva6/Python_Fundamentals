result = {}
line = 0
key = None
value = None

while True:
    command = input()
    line += 1
    if command == "stop":
        break

    elif line % 2 != 0:
        key = command

    elif line % 2 == 0:
        value = command
        if key in result:
            value = result[key] + int(value)
            result[key] = int(value)
        else:
            result[key] = int(value)


for key, value in result.items():
    print(f"{key} -> {value}")