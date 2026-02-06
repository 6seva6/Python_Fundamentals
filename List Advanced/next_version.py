version = list(map(int, input().split(".")))
def next_version(values):
    values[-1]+= 1
    if values[-1] > 9:
        values[-1] = 0
        values[1] += 1
        if values[1] > 9:
            values[1] = 0
            values[0] += 1
    return values

answer = next_version(version)
print('.'.join(map(str,answer)))
