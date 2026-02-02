a = int(input())
b = int(input())
temporary = a
print('Before:')
print(f'a = {a}')
print(f'b = {b}')
a = b
b = temporary
print('After:')
print(f'a = {a}')
print(f'b = {b}')