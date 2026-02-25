line = (input().lower()).split()
line_diction = {key:value for key, value in enumerate(line)}
result = []

for i in range (len(line_diction)):
    counter = 0
    for j in range (len(line_diction)):
        if line_diction[i] == line_diction[j]:
            counter += 1

    if counter % 2 == 0:
        continue
    else:
        if line_diction[i] not in result:
            result.append(line_diction[i])

print(' '.join(result))

