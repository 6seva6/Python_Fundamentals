str_input = str(input())
num = int(input())

repeat_string = lambda a, b: a*b
result = repeat_string(str_input, num)
print(result)