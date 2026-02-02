def calculations(operator = type[str], num1 = type[int], num2 = type[int]):
    result = 0
    if operator == "multiply":
        result = num1 * num2
    elif operator == "divide":
        result = num1/num2
    elif operator == "add":
        result = num1+num2
    elif operator == "subtract":
        result = num1-num2
    return result


print(calculations(input(), int(input()),int(input())))

