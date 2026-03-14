raw_input_data = input().split()
input_data = [value.strip() for value in raw_input_data]
alphabet_position = {
    'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6,
    'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12,
    'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18,
    'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24,
    'Y' : 25, 'Z' : 26
}


def calculations(data: list)-> int:
    result = 0
    for list_value in data:
        result += operation(list_value)
    return result

def operation(value: str) -> int:
    operation_1 = 0
    operation_2 = 0
    number = int(value[1:-1])
    letter_position = alphabet_position[(value[0]).upper()]
    if value[0].isupper():
        operation_1 = number / letter_position
    elif value[0].islower():
        operation_1 = number * letter_position
    if value[-1].isupper():
        letter_position = alphabet_position[(value[-1]).upper()]
        operation_2 = operation_1 - letter_position
    elif value[-1].islower():
        letter_position = alphabet_position[(value[-1]).upper()]
        operation_2 = operation_1 + letter_position
    return operation_2

answer = calculations(input_data)
print(f'{answer:.2f}')