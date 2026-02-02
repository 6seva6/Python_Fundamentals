number_inputs = int(input())
entire_list = []
for i in range(number_inputs):
    entire_list.append(int(input()))

filter_word = input()
filtered_list = []

for number in entire_list:
    if filter_word == "even" and number % 2 == 0:
        filtered_list.append(number)
    elif filter_word == "odd" and number % 2 != 0:
        filtered_list.append(number)
    elif filter_word == "positive" and number >= 0:
        filtered_list.append(number)
    elif filter_word == "negative" and number < 0:
        filtered_list.append(number)
print(filtered_list)
