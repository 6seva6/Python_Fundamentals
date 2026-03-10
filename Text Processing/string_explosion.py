expression = input()

result = []
strength = 0

for char in expression:
    if char == ">":
        result.append(char)
        continue
    elif char.isdigit() and result and result[-1] == ">":
        strength += int(char)
        strength -= 1
    elif strength > 0:
        strength -= 1
    else:
        result.append(char)
print("".join(result))