numbers = list(map(int,input().split(", ")))

def sorting_in_groups(sorting_list):
    """
    accpets a list of numbers, filter and return sorting groups by 10's
    """
    result = []
    current_max = int((((max(sorting_list)) + 9) // 10) * 10)
    total_groups = current_max / 10
    for _ in range (int(total_groups)):
        current_group = list(filter(lambda x: current_max - 10 <= x <= current_max, sorting_list))
        sorting_list = [num for num in sorting_list if num not in current_group]
        result.append(f"Group of {current_max}'s: {current_group}")
        current_max -= 10
    return result

for i in range(len(sorting_in_groups(numbers))-1,-1,-1):
    print((sorting_in_groups(numbers)[i]))