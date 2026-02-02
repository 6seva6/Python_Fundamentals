list_numbers = input().split(", ")

# def is_palindrome(number):
#     result = False
#     if len(number) == 1:
#         result = True
#     elif len(number) % 2 == 0:
#         half = len(number) // 2
#         left_side = number[:half]
#         right_side = number[half:][::-1]
#         if left_side == right_side:
#             result = True
#     elif len(number) % 2 != 0:
#         even = len(number) - 1
#         half = (even // 2) + 1
#         left_side = number[:half - 1]
#         right_side = number[half:][::-1]
#         if left_side == right_side:
#             result = True
#     return result
#
# for num in list_numbers:
#     print(is_palindrome(num))

def is_palindrome2(number2):
    return number2 == number2[::-1]

for num in list_numbers:
    print(is_palindrome2(num))