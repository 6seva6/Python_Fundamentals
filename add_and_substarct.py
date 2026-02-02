def summ_numbers (num1, num2):
    return num1 + num2

def substract_numbers (summ, num3):
    return summ - num3

a = int(input())
b = int(input())
c = int(input())

summ_of_numbers = summ_numbers(a,b)
difference = substract_numbers(summ_of_numbers,c)
print(difference)