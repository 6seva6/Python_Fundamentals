import re

key = [int(value) for value in input().split()]
encrypt_message = []
decrypted_messages = []
old_key_len = len(key)

while (message:= input()) != 'find':
    encrypt_message.append(message)

for value in encrypt_message:

    current_index = 0
    current_key = key.copy()


    while len(current_key) < len(value):
        if current_index == old_key_len:
            current_index = 0
        current_key.append(current_key[current_index])
        current_index += 1

    key_index = 0
    decrypted_message = ''

    for char in value:
        letter = chr(ord(char) - current_key[key_index])
        decrypted_message += letter
        key_index += 1

    decrypted_messages.append(decrypted_message)

pattern_treasure_type = r'&(\w+)&'
pattern_coordinates = r'<([A-Z0-9]+)>'

for output in decrypted_messages:
    match_treasure_type = re.search(pattern_treasure_type, output)
    match_coordinates = re.search(pattern_coordinates, output)
    print(f'Found {match_treasure_type.group(1)} at {match_coordinates.group(1)}')