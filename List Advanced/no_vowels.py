input_word = str(input())
input_word = [char for char in input_word if char.lower() not in 'aeiou']
print(''.join(input_word))