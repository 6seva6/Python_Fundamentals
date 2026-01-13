devisor = int(input())
boundary = int(input())

for i in range(boundary, devisor, -1):
    if i % devisor == 0:
        print(i)
        break