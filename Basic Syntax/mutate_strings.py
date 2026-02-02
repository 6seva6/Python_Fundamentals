string_1 = str(input())
string_2 = str(input())

for i in range(len(string_1)):
    mutated_string = ''
    if string_1[i] != string_2[i]:
        mutated_string = string_2[:i+1] + string_1[i+1:]
        print(mutated_string)
    else:
        continue