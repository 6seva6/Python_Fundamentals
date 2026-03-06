usernames = input().split(', ')

def length_is_valid(username_:str) -> bool:
    if 3 <= len(username_) <= 16:
        return True
    return False

def char_is_valid(username_:str) -> bool:
    for char in username_:
        if not(char.isalnum() or char=='_' or char== '-'):
            return False
    return True

def valid_symbols(username_:str) -> bool:
    if ' ' in username_:
        return False
    return True

def username_is_valid(username_ : str) -> bool:
    if length_is_valid(username_) and char_is_valid(username_) and valid_symbols(username_):
        return True
    return False


for username in usernames:
    if username_is_valid(username):
        print(username)