lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expensis = 0
for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        expensis += helmet_price
    if i % 3 == 0:
        expensis += sword_price
    if i % 6 == 0:
        expensis += shield_price
    if i % 12 == 0:
        expensis += armor_price
print(f'Gladiator expenses: {expensis:.2f} aureus')