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
    else:
        return cities_, f'{robed_city} plundered! {stolen_gold} gold stolen, {killed_people} citizens killed.', None

def prosper(cities_, args_):
    pass

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
    print(message1)
    print(cities)