line_numbers = int(input())
key_word = input()
entire_list = []
filtered_list = []

for i in range(line_numbers):
    entire_list.append(input())
print(entire_list)

for i in range(len(entire_list)):
    element = entire_list[i]
    if key_word in element:
        filtered_list.append(element)
print(filtered_list)