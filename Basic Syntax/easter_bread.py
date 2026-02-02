budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
price_per_bread = flour_price + egg_price + (milk_price / 4)
current_bread_count = 0
money_left = budget
colored_eggs = 0
while money_left >= price_per_bread:
    money_left -= price_per_bread
    current_bread_count += 1
    colored_eggs += 3

    if current_bread_count % 3 == 0:
        colored_eggs = colored_eggs - (current_bread_count - 2)

print(f'You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')

