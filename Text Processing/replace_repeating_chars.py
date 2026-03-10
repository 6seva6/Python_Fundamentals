repeated_letters = input()

filtered_text = ''

for index in range(len(repeated_letters)):
    if not filtered_text:
        filtered_text += repeated_letters[index]
    elif  repeated_letters[index] != filtered_text[-1]:
        filtered_text += repeated_letters[index]
    else:
        continue

print(filtered_text)
