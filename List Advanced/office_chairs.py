number_of_rooms = int(input())
def chairs_calculations(rooms):
    """
    Return number of free chairs left in the room or number of needed chairs.
    :param rooms: list of rooms
    :return: result
    """
    result = []
    free_chairs = 0
    for room in range(1, rooms+1):
        curr_room_data = [ data for data in input().split()]
        if int(curr_room_data[1]) > len(curr_room_data[0]):
            result.append(f"{int(curr_room_data[1]) - len(curr_room_data[0])} more chairs needed in room {room}")
        else:
            free_chairs += len(curr_room_data[0]) - int(curr_room_data[1])
    if result == []:
        result.append(f"Game On, {free_chairs} free chairs left")
    return result

resolution = chairs_calculations(number_of_rooms)
for i in range(len(resolution)):
    print(resolution[i])
