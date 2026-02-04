potential_palindromes = input().split()
desired_palindrome = str(input())

def is_palindrome(value_list, key_palindrome):

    palindromes = [value for value in value_list if value==value[::-1]]
    palindrome_count = palindromes.count(key_palindrome)
    return palindromes, palindrome_count

palindromes, counter = is_palindrome(potential_palindromes, desired_palindrome)

print(palindromes)
print(f"Found palindrome {counter} times")