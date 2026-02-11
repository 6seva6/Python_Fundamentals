initial_list = [ groceries for groceries in input().split("!")]
shopping_list = initial_list
command=[]
while command!=["Go", "Shopping!"]:
    command = [ item for item in input().split()]
    if command[0]=="Urgent" and command[1] not in shopping_list:
        shopping_list.insert(0,command[1])
    elif command[0]=="Unnecessary" and command[1] in shopping_list:
        shopping_list.remove(command[1])
    elif command[0]=="Correct" and command[1] in shopping_list:
        shopping_list[shopping_list.index(command[1])] = command[2]
    elif command[0] == "Rearrange" and command[1] in shopping_list:
        removed_item = shopping_list.pop(shopping_list.index(command[1]))
        shopping_list.append(removed_item)

print(", ".join(shopping_list))