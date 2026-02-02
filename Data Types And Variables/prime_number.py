count = 0
result = None
for i in range(1, number + 1):
    if number % i == 0:
        count += 1
    if count <= 2:
        result = 'True'
    else:
        result = 'False'
print(result)