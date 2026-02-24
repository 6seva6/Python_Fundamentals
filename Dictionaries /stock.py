products = input().split()
result = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i + 1])
    result[key] = value

searching_products = input().split()

for key in searching_products:
    if key in result:
        print(f"We have {result[key]} of {key} left")

    else:
        print(f"Sorry, we don't have {key}")