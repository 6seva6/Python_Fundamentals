password = input()

def is_password_valid(password_):
    length_check = None
    letter_digit_check = None
    digits_check = None
    final_check = None

    if 10 > len(password) < 6:
        length_check = "Password must be between 6 and 10 characters"
    digit_count = 0
    for char in password:
        char_value = ord(char)
        if not (
            48 <= char_value <= 57 or
            65 <= char_value <= 90 or
            97 <= char_value <= 122):
            letter_digit_check = "Password must consist only of letters and digits"
            continue
        if 48 <= char_value <= 57:
            digit_count += 1
    if digit_count < 2:
        digits_check = "Password must have at least 2 digits"
    elif length_check == None and letter_digit_check == None and digits_check == None:
        final_check = "Password is valid"
    return length_check, letter_digit_check, digits_check, final_check

answer = is_password_valid(password)

for result in answer:
    if result is not None:
        print(result)