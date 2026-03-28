coded_message = input()
commands = []

def encrypt(args, message):
    message = message[::-1]
    return message, None

def decrypt(args, message):
    temp_message = ''
    for char in message:
        if char in '0123456789':
            temp_message += char
        elif char.islower():
            temp_message += char.upper()
        elif char.isupper():
            temp_message += char.lower()
    return temp_message, None

def substitute(args, message):
    old_char, new_char = args
    if old_char not in message:
        return message, f'Character not found.'
    else:
        return message.replace(old_char, new_char), None

def scramble(args, message):
    index, char = args
    index = int(index)
    if not 0 <= index < len(message):
        return message, f'Index out of bounds.'

    message = message[:index] + char + message[index + 1:]
    return  message, None

def remove(args, message):
    substring = args[0]
    return message.replace(substring, ''), None

commands = {
    "Encrypt" : encrypt,
    "Decrypt" : decrypt,
    "Substitute" : substitute,
    "Scramble" : scramble,
    "Remove" : remove
}

while (command:= input()) != 'Finalize':
    parts = command.split()
    command = parts.pop(0)

    if command not in commands:
        print(f'Invalid command detected!')
    else:
        coded_message, error_message = commands[command](parts, coded_message)
        if error_message:
            print(error_message)
            continue
        print(coded_message)