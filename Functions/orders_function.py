def orders(product, quantity):
    result = None
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity * 1
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2.00
    return result

item = str(input())
number = int(input())

output = orders(item, number)
print(f"{output:.2f}")