class Party:
    def __init__(self):
        self.names = []

party = Party()

while True:
    command = input()
    if command == "End":
        break
    party.names.append(command)

print(f"Going: {' '.join(party.names)}")
print(f"Total: {len(party.names)}")