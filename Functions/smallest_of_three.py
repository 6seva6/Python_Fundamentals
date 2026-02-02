def smallest_number(num1 = type(int),num2 = type(int),num3 = type(int)):
    list_int = []
    for num in (num1,num2,num3):
        list_int.append(num)
    sorted_list = sorted(list_int)
    return sorted_list[0]

a = int(input())
b = int(input())
c = int(input())

result = smallest_number(a,b,c)
print(result)