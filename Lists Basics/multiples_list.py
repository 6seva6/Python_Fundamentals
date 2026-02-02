count = int(input())
factor = int(input())
output = []

for number in range(1,factor + 1):
    output.append(count*number)
print(output)