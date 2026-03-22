initial_stops = input()

def add_stop(message, parts_):
    index, string = parts_
    index = int(index)
    if 0 <= index <= len(message):
        message = message[:index] + string + message[index:]
        return message
    return message

def remove_stop(message, parts_):
    start_index, stop_index = parts_
    start_index = int(start_index)
    stop_index = int(stop_index)
    if 0 <= start_index < stop_index and start_index < stop_index + 1 <= len(message):
        message = message[:start_index] + message[stop_index + 1:]
        return message
    return message

def switch(message, parts_):
    old_string, new_string = parts_
    if old_string in message:
        message = message.replace(old_string, new_string)
        return message
    return message

actions = {
    'Add Stop' : add_stop,
    'Remove Stop' : remove_stop,
    'Switch' : switch
}

while (commands:= input())!="Travel":
    parts = commands.split(':')
    command = parts.pop(0)

    initial_stops = actions[command](initial_stops, parts)
    print(initial_stops)

print(f'Ready for world tour! Planned stops: {"".join(initial_stops)}')