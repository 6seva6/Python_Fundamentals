input_strings = input().split()
diff = 0

if len(input_strings[0]) != len(input_strings[1]):
    if len(input_strings[1]) > len(input_strings[0]):
        diff = len(input_strings[1]) - len(input_strings[0])
        temp = input_strings[0]
        input_strings[0] = input_strings[1]
        input_strings[1] = temp
    else:
        diff = len(input_strings[0]) - len(input_strings[1])
summ = 0
for char in range(len(input_strings[0])):
    if char >= len(input_strings[0])- diff:
        summ +=  ord(input_strings[0][char])
    else:
        summ += ord(input_strings[0][char]) * ord(input_strings[1][char])

print(summ)