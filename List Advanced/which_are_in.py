substr_list = [x for x in input().split(", ")]
str_list = [x for x in input().split(", ")]
def are_in(compare, instance):
    result = []
    for i in compare:
        for j in range(len(instance)):
            if i in str_list[j]:
                result.append(i)
    return result
answer = sorted((list(set(are_in(compare=substr_list, instance=str_list)))), key = lambda x: x)
print(answer)