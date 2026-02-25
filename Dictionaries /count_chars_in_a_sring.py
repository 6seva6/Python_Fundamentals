string_ = input()
output = {}

for i in range(len(string_)):
    if string_[i] != ' ':
        temp_key = string_[i]
        if temp_key in output:
            continue
    else:
        continue
    counter = 0
    for j in range(len(string_)):
        temp_value = string_[j]
        if temp_key == temp_value:
            counter += 1
            output[temp_key] = counter

for key, value in output.items():
    print(f"{key} -> {value}")