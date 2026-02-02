list_str_number = input().split()

def rounding (list):
    result = []
    for item in list:
        result.append(round(float(item)))
    return result

convertation = rounding(list_str_number)
print(convertation)
