phone_book = {}
contacts_quantity_search = None

while True:
    command = input().split("-")
    if command[0] in '0123456789':
        contacts_quantity_search = int(command[0])
        break
    phone_book[command[0]] = command[1]

for i in range(contacts_quantity_search):
    search_name = input()
    if search_name in phone_book:
        print(f"{search_name} -> {phone_book[search_name]}")

    else:
        print(f"Contact {search_name} does not exist.")

