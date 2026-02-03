from math import sqrt
input_coordinates = []


for i in range(0, 8):
    input_coordinates.append(input())
    if "." in input_coordinates[i]:
        input_coordinates[i] = float(input_coordinates[i])
    else:
        input_coordinates[i] = int(input_coordinates[i])


def longer_line(coordinates):
    first_line_coordinates = coordinates[:4]
    second_line_coordinates = coordinates[4:]
    sum_first_line = sqrt((first_line_coordinates[2] - first_line_coordinates[0]) **2 + (first_line_coordinates[3] - first_line_coordinates[1]) **2 )
    sum_second_line = sqrt((second_line_coordinates[2] - second_line_coordinates[0]) **2 + (second_line_coordinates[3] - second_line_coordinates[1]) **2 )
    if sum_first_line >= sum_second_line:
        result = first_line_coordinates
    else:
        result = second_line_coordinates
    if abs(result[0]) + abs(result[1]) > abs(result[2])+abs(result[3]):
        result = [result[2], result[3], result[0], result[1]]
    return result

answer = longer_line(input_coordinates)
print(f"({answer[0]}, {answer[1]})({answer[2]}, {answer[3]})")