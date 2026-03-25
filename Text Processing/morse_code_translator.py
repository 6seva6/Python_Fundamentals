alphabet = {
    '.-' : 'A', '-...' : 'B', '-.-.' : 'C',
    '-..' : 'D', '.' : 'E', '..-.' : 'F',
    '--.' : 'G' , '....' : 'H', '..' : 'I',
    '.---' : 'J', '-.-' : 'K', '.-..' : 'L',
    '--' : 'M', '-.' : 'N', '---' : 'O',
    '.--.' : 'P', '--.-' : 'Q', '.-.' : 'R',
    '...' : 'S' , '-' : 'T', '..-' : 'U',
    '...-' : 'V', '.--' : 'W', '-..-' : 'X',
    '-.--' : 'Y', '--..' : 'Z'
}

encode_sentence = input().split('|')
encode_sentence = [word.strip() for word in encode_sentence]
message = ''

for word in encode_sentence:
    word_letters = (''.join(word)).split()
    decoded_word = ''
    for letter in word_letters:
        decoded_letter = alphabet[letter]
        decoded_word += decoded_letter
    message += decoded_word + ' '

print(message)