budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price = flour_price * 1.25
bread_price = flour_price + egg_price + milk_price * 0.25

loaves = 0
eggs = 0
money_left = budget

while money_left >= bread_price:
    money_left -= bread_price
    loaves += 1
    eggs += 3

    if loaves % 3 == 0:
        eggs -= (loaves - 2)

print(
    f"You made {loaves} loaves of Easter bread! "
    f"Now you have {eggs} eggs and {money_left:.2f}BGN left."
)