number_lines = int(input())
positive = []
negative = []

for i in range(number_lines):
    digit = int(input())
    if digit >= 0:
        positive.append(digit)
    else:
        negative.append(digit)
print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
