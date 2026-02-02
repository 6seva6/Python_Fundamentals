group_size = int(input())
days = int(input())
expensis = 0
earnings = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size += -2
    if i % 15 == 0:
        group_size += +5
    earnings += 50
    expensis += 2 * group_size
    if i % 3 ==0:
        expensis += 3* group_size
    if i % 5 == 0:
        earnings += group_size * 20
        if i % 3 == 0:
            expensis += group_size * 2

earnings = earnings - expensis
coins_per_person = int(earnings / group_size)
print(f'{group_size} companions received {coins_per_person} coins each.')