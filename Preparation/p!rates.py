cities = {}

while (city:= input()) != 'Sail':
    city_data = city.split('||')
    key = city_data.pop(0)
    value = [int(value) for value in city_data]
    if key in cities:
        population, gold = value
        cities[key][0] += population
        cities[key][1] += gold
    else:
        cities[key] = value

def plunder(cities_, args_):
    robed_city, killed_people, stolen_gold = args_
    cities_[robed_city][0] -= killed_people
    cities_[robed_city][1] -= stolen_gold
    if cities_[robed_city][0] <= 0 or cities_[robed_city][1] <= 0:
        del cities_[robed_city]
        return cities_, f'{robed_city} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.', f'{robed_city} has been wiped off the map!'

    return cities_, f'{robed_city} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.', None

def prosper(cities_, args_):
    city, returned_gold = args_
    if returned_gold < 0:
        print(f'Gold added cannot be a negative number!')
        return cities_, None, None

    cities_[city][1] += returned_gold
    return cities_, f'{returned_gold} gold added to the city treasury. {city} now has {cities_[city][1]} gold.', None

instructions_for_commands = {
    'Plunder' : plunder,
    'Prosper' : prosper
}

while (command:= input()) != 'End':
    commands = command.split('=>')
    command = commands.pop(0)
    args = []
    for i in range(len(commands)):
        if i > 0:
         args.append(int(commands[i]))
        else:
            args.append(commands[i])

    cities, message1, message2 = instructions_for_commands[command](cities, args)
    if message1:
        print(message1)
    if message2:
        print(message2)

print(f'Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:')

for key, value in cities.items():
    print(f'{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg')