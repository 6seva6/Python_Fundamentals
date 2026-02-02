key = int(input())
iteration = int(input())

for i in range(iteration):
    incrypt_letter = input()
    decrypt_letter = chr(key + ord(incrypt_letter))
    print(decrypt_letter)