food = input().split()
result = {}

for i in range(0, len(food), 2):
    key = food[i]
    value = int(food[i+1])
    result[key] = value

print(result)
