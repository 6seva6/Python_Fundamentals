input_number = int(input())

def tribonacci(number):
    result = [0]*number
    for i in range(number):
        if i == 0 or i == 1:
            result[i] = 1
        elif i == 2:
            result[i] = 2
        else:
            result[i] = (result[i-1])+(result[i-2])+(result[i-3])
    return result

answer = tribonacci(input_number)
for i in range(len(answer)):
    print(answer[i],end=" ")
