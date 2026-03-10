input_text = input()

for index in range(len(input_text)):
    if input_text[index] == ':':
        print((input_text[index] + input_text[index + 1]))
    else:
        continue
