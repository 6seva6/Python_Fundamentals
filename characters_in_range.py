def characters_in_range(start, end):
    start_index = ord(start)
    end_index = ord(end)
    for i in range(start_index+1,end_index):
        print(chr(i), end=" ")

a = input()
b = input()
characters_in_range(a,b)