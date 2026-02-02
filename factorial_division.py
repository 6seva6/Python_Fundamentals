num1= int(input())
num2= int(input())

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

factorial_1 = factorial(num1)
factorial_2 = factorial(num2)
answer = factorial_1 / factorial_2

print(f"{answer:.2f}")