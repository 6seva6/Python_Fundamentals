input_path = input().split('\\')
file = input_path[-1]
index = file.find('.')
name = file[:index]
extension = file[index+1:]
print(f'File name: {name}')
print(f'File extension: {extension}')