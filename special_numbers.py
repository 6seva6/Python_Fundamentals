number = int(input())

for digit in range(1, number + 1):
    digit_summ = 0
    num = digit
    while digit > 0:
        digit_summ += digit % 10
        digit = int(digit / 10)
    if digit_summ == 5 or digit_summ == 7 or digit_summ == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')