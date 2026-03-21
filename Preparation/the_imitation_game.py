message = input()

def move(message_, parts_):
    n_letters = int(parts_[0])
    message_ = message_[n_letters:] + message_[:n_letters]
    return message_

def insert_(message_, parts_):
    index = int(parts_[0])
    value = parts_[1]
    message_ = message_[:index] + value + message_[index:]
    return message_

def changeall(message_, parts_):
    substrings = parts_[0]
    replacement = parts_[1]
    message_ = message_.replace(substrings, replacement)
    return message_

actions = {
    'Move': move,
    'Insert': insert_,
    'ChangeAll': changeall
}

while (commands:= input()) != 'Decode':
    parts = commands.split('|')
    command = parts[0]
    args = parts[1:]

    message = actions[command](message, args)

print(f'The decrypted message is: {message}')