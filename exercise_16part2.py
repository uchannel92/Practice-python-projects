print('Uchenna Attah\nPassword generator v.01\n')
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords 
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# easy
# password length 8 10 12 - user will choose that length
# 08 ---> 6 letter == 1 number, 1 sumbol 
# 10 ---> 6 letter == 2 number, 2 symbol
# 12 ---> 6 letter == 3 number, 3 symbol

# prompt for a passsword length
# prompt for special charactes
# prompt for numbers
from random import choice, choices ,shuffle, sample

def get_password_length():

    prompt = '''Hello.\nPlease Enter the number for Password length you would like:\n
    1) Default: (8 characters)
    2) Medium: (10 characters)
    3) Hard: (12 characters)\n: '''

    pasword_length = int(input(prompt))

    return pasword_length


def get_password_params(password_length='', numbers_included='', symbols_included=''):


    password_parameters = []
    
    if password_length == 1:

        password_length = 6
        numbers_included = 1
        symbols_included = 1
        password_parameters.append(password_length)
        password_parameters.append(numbers_included)
        password_parameters.append(symbols_included)

    elif password_length == 2:

        password_length = 6
        numbers_included = 2
        symbols_included = 2
        password_parameters.append(password_length)
        password_parameters.append(numbers_included)
        password_parameters.append(symbols_included)

    elif password_length == 3:

        password_length = 6
        numbers_included = 3
        symbols_included = 3
        password_parameters.append(password_length)
        password_parameters.append(numbers_included)
        password_parameters.append(symbols_included)

    # print(password_parameters)
    return password_parameters


def generate_a_password(password_parameters):

    print(f'password params: {password_parameters}')

    lower_upper = ''

    letters = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z'
    ]
    numbers = [
        '0', '1', '2', 
        '3', '4', '5', 
        '6', '7', '8', 
        '9'
    ]
    symbols = [
    '!', '@', '£', '$', '%', 
    '^', '&', '*', '-', '+',
    ]

    random_letters = (choices(letters, k=password_parameters[0]))
    random_numbers = (choices(numbers, k=password_parameters[1]))
    random_symbols = choices(symbols, k=password_parameters[2])

    for letter in random_letters:
        if choice((True, False)):
            lower_upper += letter.upper()
        else:
            lower_upper += letter

    password_string = lower_upper.split() + random_numbers + random_symbols
    shuffle_string = sample(password_string, len(password_string))
    joined_password_string = ''.join(shuffle_string)
    
    print(password_string)
    print(shuffle_string)
    print('---')
    # print(joined_password_string)
    return f'You new password is:\n{joined_password_string}'



# returns a number 1, 2, 3 to correspond to the length of password required.
password_length = get_password_length()

# returns password_parameters
password_test_variable = get_password_params(password_length)

# accepts password_params to create password.
generate_password = generate_a_password(password_test_variable)
print(generate_password)



