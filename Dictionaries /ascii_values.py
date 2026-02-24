characters = input().split(", ")

final_characters = {x: ord(x) for x in characters}

print(final_characters)