country_names = [country for country in input().split(", ")]
capitals = [capital for capital in input().split(", ")]
result = {country_names[i]:capitals[i] for i in range(len(capitals))}

for key, value in result.items():
    print(f"{key} -> {value}")