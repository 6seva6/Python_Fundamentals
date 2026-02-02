def summ_of_odd_even (number):
    odd_sum = 0
    even_sum = 0
    number = str(number)
    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return odd_sum, even_sum

num = int(input())
result_odd, result_even = summ_of_odd_even(num)
print(f"Odd sum = {result_odd}, Even sum = {result_even}")



