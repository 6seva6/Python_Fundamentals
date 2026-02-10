incypted_message = [word for word in input().split()]
command = [command for command in input().split()]
decrypted_message = incypted_message

while command != ['3:1']:
    if command[0]== 'merge':
        left_side = ''
        merged_value = ''
        right_side = ''
        start_index = int(command[1])
        end_index = int(command[2])

        if  start_index < 0 or start_index > len(decrypted_message)-1:
            start_index = 0
        if end_index > len(decrypted_message)-1:
            end_index = len(decrypted_message) -1
            if decrypted_message[0]== decrypted_message[-1]:
                break

        left_side = [decrypted_message[i] for i in range(len(decrypted_message)) if i < start_index]

        for i in range (start_index, end_index + 1):
                merged_value += decrypted_message[i]
        right_side = [decrypted_message[i] for i in range(len(decrypted_message)) if i > end_index]

        decrypted_message = [*left_side, merged_value, *right_side]
    if command[0] == 'divide':

        left_side = ''
        divide_value = []
        right_side = ''
        divide_string_index = int(command[1])
        if divide_string_index > len(decrypted_message)-1:
            end_index = len(decrypted_message) -1
        divided_string_itself = decrypted_message[divide_string_index]
        divisor = int(command[2])
        substring_len = len(divided_string_itself) // divisor


        left_side = [decrypted_message[i] for i in range(len(decrypted_message)) if i < divide_string_index]
        start_index = 0
        for i in range(divisor):
            if i == divisor -1:
                divide_value.append(divided_string_itself[start_index:])
            else:
                divide_value.append(divided_string_itself[start_index:start_index + substring_len])
                start_index += substring_len

        right_side = [decrypted_message[i] for i in range(len(decrypted_message)) if i > divide_string_index]
        decrypted_message = [*left_side, *divide_value, *right_side]

    command = [command for command in input().split()]

print(' '.join(decrypted_message))