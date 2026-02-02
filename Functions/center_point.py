x1 = input()
y1 = input()
x2 = input()
y2 = input()

def value_type(x1_,y1_,x2_,y2_):
    result = [x1_,y1_,x2_,y2_]
    index = 0
    for i in result:
        if "." in i:
            result[index]=float(result[index])
        else:
            result[index]=int(result[index])
        index+=1
    return result

def closest_point(x1_,y1_,x2_,y2_):
    result = None
    values = value_type(x1_,y1_,x2_,y2_)
    point_1 = abs(values[0]) + abs(values[1])
    point_2 = abs(values[2]) + abs(values[3])
    if point_1 < point_2:
        result = [values[0],values[1]]
    else:
        result = [values[2], values[3]]
    return result

answer = closest_point(x1,y1,x2,y2)
print(f"({int(answer[0]) }, {int(answer[1])})")