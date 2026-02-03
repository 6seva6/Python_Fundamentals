numbers = []
for i in range(3):
    numbers.append(input())

def multiplication_sign(list_):
    counter = 0
    zero = ""
    for number in list_:
        if "-" in number:
            counter += 1
        if number == "0":
            zero = "zero"
            break
    if counter % 2 == 0 or counter == 0:
        result = "positive"
    else:
        result = "negative"
    if zero != "":
        result = "zero"
    return result

answer = multiplication_sign(numbers)
print(answer)