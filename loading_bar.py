loading_percent = int(input())

def loading_bar(num):
    percent_bar = ['.']*10
    message = "Still loading..."
    if num == 100:
        percent_bar = ["%"] * 10
        message = "Complete!"
    else:
        for i in range(num//10):
            percent_bar[i] = "%"
    return percent_bar, message

first_line, second_line = loading_bar(loading_percent)
first_line_string = ''
for item in first_line:
    first_line_string += item

if loading_percent == 100:
    print(f"{loading_percent}% {second_line}")
    print(f"[{first_line_string}]")
else:
    print(f"{loading_percent}% [{first_line_string}]")
    print(second_line)