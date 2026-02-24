products = {}

while True:
    command = input().split(': ')
    if command[0] == "statistics":
        print(f"Products in stock:")
        for key, value in products.items():
            print(f"- {key}: {value}")
        count_all_products = len(products)
        sum_all_quantities = sum(products.values())
        print(f"Total Products: {count_all_products}\nTotal Quantity: {sum_all_quantities}")
        break
    else:
        if command[0] in products:
            products[command[0]] += int(command[1])
        else:
            key = command[0]
            value = int(command[1])
            products[key] = value