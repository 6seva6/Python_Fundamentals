number_of_orders = int(input())
total_price = 0.0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    if days < 1 or days > 31:
        continue
    if capsule_per_day < 1 or capsule_per_day > 2000:
        continue
    price_per_coffe = price_per_capsule * days * capsule_per_day
    total_price += price_per_coffe
    print(f'The price for the coffee is: ${price_per_coffe:.2f}')
print(f"Total: ${total_price:.2f}")