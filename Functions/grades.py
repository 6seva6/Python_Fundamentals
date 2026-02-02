evaluation = float(input())

def grade(evaluation_):
    if 2.00 <= evaluation_ <= 2.99:
        return "Fail"
    elif 3.00 <= evaluation_ <= 3.49:
        return "Poor"
    elif 3.50 <= evaluation_ <= 4.49:
        return "Good"
    elif 4.50 <= evaluation_ <= 5.49:
        return "Very Good"
    elif 5.50 <= evaluation_ <= 6.00:
        return "Excellent"

print(grade(evaluation))