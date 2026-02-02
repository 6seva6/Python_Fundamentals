number = int(input())

def is_perfect_number(value):
    result = "It's not so perfect."
    if value % 2 == 0:
        half = value // 2
        divisors = []
        for i in range(1, half + 1):
            if value % i == 0:
                divisors.append(i)
        if sum(divisors) == number:
            result = "We have a perfect number!"
    return result

answer = is_perfect_number(number)
print(answer)
