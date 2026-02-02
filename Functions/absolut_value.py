int_num = input().split()

def string_to_float(string):
    abs_num =[]
    for i in string:
        abs_num.append(abs(float(i)))
    return abs_num

result = string_to_float(int_num)
print(result)