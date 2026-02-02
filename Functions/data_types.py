input_type = str(input())
value = input()

def data_types(type_, value_):
    result = None
    if type_ == "int":
        result = 2 * int(value_)
    elif type_ == "real":
        result = f"{1.5 * float(value_):.2f}"
    elif type_ == "string":
        result = f"${str(value_)}$"
    return result

answer = data_types(input_type, value)
print(answer)