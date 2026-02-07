sipher_message = [message for message in input().split()]

def decipher_this(messages):
    """
    Decipher messages
    :param messages: sipher messages
    """
    result = []
    for i in range(len(messages)):
        number_values = ''.join([value for value in messages[i] if value in '0123456789'])
        string_values = [value for value in messages[i] if value not in number_values]
        first_letter = chr(int(number_values))
        tempo_variable = string_values[0]
        string_values[0] = string_values[-1]
        string_values[-1] = tempo_variable
        result.append(first_letter + ''.join(string_values))
    return result

print(' '.join(decipher_this(sipher_message)))