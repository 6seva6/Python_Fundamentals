chars_quantity = int(input())
char_sum = 0

for i in range(chars_quantity):
    char = input()
    char_sum += ord(char)
print(f'The sum equals: {char_sum}')