junk = {}
legendary_items = {"Shadowmourne": {"shards": 0},
                   "Valanyr": {"fragments": 0},
                   "Dragonwrath":{"motes": 0}}
def is_true():
    return (
    legendary_items["Shadowmourne"]["shards"] > 250 or
    legendary_items["Valanyr"]["fragments"] > 250 or
    legendary_items["Dragonwrath"]["motes"] > 250
    )

while True:
    if is_true():
        break
    all_items = input().lower().split()

    for i in range(0, len(all_items), 2):
        if any( all_items[i + 1] in inner_dict for inner_dict in legendary_items.values()) :
            if all_items[i + 1] == "shards":
                legendary_items["Shadowmourne"]["shards"] += int(all_items[i])
                if is_true():
                    break
            elif all_items[i + 1] == "fragments":
                legendary_items["Valanyr"]["fragments"] += int(all_items[i])
                if is_true():
                    break
            elif all_items[i + 1] == "motes":
                legendary_items["Dragonwrath"]["motes"] += int(all_items[i])
                if is_true():
                    break

        else:
            if is_true():
                break
            else:
                key = all_items[i + 1]
                value = all_items[i]
                junk[key] = junk.get(key, 0) + int(value)


for key, value in legendary_items.items():
    amount = list(value.values())[0]

    if amount > 250:
        legendary_items[key][list(value.keys())[0]] -= 250
        print(f"{key} obtained!")
        for inside_key, inside_value in legendary_items.items():
            print(f"{list(inside_value.keys())[0]}: {legendary_items[inside_key][list(inside_value.keys())[0]]}")

for key, value in junk.items():
    print(f"{key}: {value}")