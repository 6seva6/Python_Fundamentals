message = ' '.join(input().split())
ciphered_message = ''

for char in message:
    right_shift = 3
    current_char = (ord(char) + right_shift) % 256
    ciphered_message += chr(current_char)

print(ciphered_message)