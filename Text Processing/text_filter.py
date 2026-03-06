filtered_words = input().split(', ')

text = input()

for word in filtered_words:
    while word in text:
        new_text = text.replace(word, len(word) * '*')
        text = new_text

print(text)