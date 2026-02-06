words_list = [word for word in input().split(' ')]
filtered_list = list(filter(lambda x: len(x)%2==0, words_list))
# filtered_list = [word for word in words_list if len(word)%2==0]
for i in range (len(filtered_list)):
    print(filtered_list[i])