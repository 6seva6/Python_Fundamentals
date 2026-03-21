car_quantity = int(input())
cars = {}

for _ in range(car_quantity):
    raw_input = input().split('|')
    key = raw_input.pop(0)
    value = [int(value) for value in raw_input]
    cars[key] = value

def drive(arguments_):
    car_for_driving, distance, required_fuel = arguments_
    car_for_driving = car_for_driving.strip()
    car_fuel = int(cars[car_for_driving][1])

    if car_fuel < required_fuel:
        return 'Not enough fuel to make that ride'
    elif car_fuel >= required_fuel:
        cars[car_for_driving][0] += distance
        cars[car_for_driving][1] -= required_fuel
        return f"{car_for_driving} driven for {distance} kilometers. {required_fuel} liters of fuel consumed."

def refuel(arguments_):
    car_for_driving, add_fuel = arguments_
    car_for_driving = car_for_driving.strip()
    fuel_in_tank = cars[car_for_driving][1]

    if fuel_in_tank + add_fuel > 75:
        added = 75 - fuel_in_tank
        cars[car_for_driving][1] = 75
    else:
        added = add_fuel
        cars[car_for_driving][1] += add_fuel

    return f"{car_for_driving} refueled with {added} liters"

def revert(arguments_):
    car_for_driving, removed_mileage = arguments_
    car_for_driving = car_for_driving.strip()
    current_mileage = cars[car_for_driving][0]
    if current_mileage - removed_mileage > 10000:
        cars[car_for_driving][0] = current_mileage - removed_mileage
        return f"{car_for_driving} mileage decreased by {removed_mileage} kilometers"
    else:
        cars[car_for_driving][0] = 10000
actions = {
    'Drive' : drive,
    'Refuel' : refuel,
    'Revert' : revert
}

while (commands:= input()) != 'Stop':
    instruction = commands.split(':')
    command = (instruction[0]).strip()
    arguments = instruction[1:]
    for index, value in enumerate(arguments):
        if index > 0:
            arguments[index] = int(value)
    output = actions[command](arguments)
    if output:
        print(output)

    car = arguments[0].strip()
    if cars[car][0] >= 100000:
        print (f"Time to sell the {car}!")
        del cars[car]

for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")