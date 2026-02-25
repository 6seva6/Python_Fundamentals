words = int(input())
synonyms = {}

for i in range(0, words):
    key = input()
    value = input()
    if key not in synonyms:
        synonyms[key] = [value]
    else:
        synonyms[key].append(value)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
