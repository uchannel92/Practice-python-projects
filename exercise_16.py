# Password generator
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords 
# have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

# prompt 4 questions to get a random password generated.

from random import choice
# choose a list of randomly generated questions to generate a password

def generate_a_random_question():
    # Pull a random question from the question array.
    # These question will be used to generate a random password.

    questions = [
        'Enter your favourite city: ', 'Enter your favourite colour: ', 'Enter your second best dish (one-word): ',
        'Enter the name of your favourite pet: ', 'Enter the name of your favourite sports brand: ', 
        'Enter your name spelt backwards?: ', 'Enter your favourite animal: ' , 'Enter your favourite form of exercise: '
    ]

    random_question = choice(questions)

    return random_question


def generate_a_password():

    answers = []
    asked_questions = []

    genrate_question = generate_a_random_question()
    asked_questions.append(genrate_question)

    # Originally this will be four questions, changing to two to make my life easier for now.
    while len(answers) != 4:

        check_question = generate_a_random_question()

        if check_question in asked_questions:
            # If the random question has already been asked, skip and ask a new question.
            pass
        else:
            # Ask the next unanswered question, and add to password container.
            print('In ONE word, answer the following: ')
            next_question = input(check_question)
            asked_questions.append(check_question)
            answers.append(next_question)

    return answers


def generate_random_numbers():
    # extract two random numbers from this list

    numbers = list(range(10))
    random_numbers = []
    numbers_string = ''

    # two numbers to be returned in password
    for number in range(2):
        random_numbers.append(str(choice(numbers)))
        
    number_string = ''.join(random_numbers)

    return number_string


def generate_random_symbol():
    # extract two random symbols from this list
    symbols = [
        '!', '@', '£', '$', '%', 
        '^', '&', '*', '-', '+', 
        '_',
    ]

    random_symbols = []
    
    for symbol in range(1):
        random_symbols.append(choice(symbols))
        
    return ''.join(random_symbols)


def create_string(step_one):
    
    new_password = []
    # Accept the list of accepted ansers this will be the return value from the answers.
    answers = step_one

    for answer in answers:
        # grab the middle two characters
        if len(answer) % 2 == 0:
            middle_index = round(len(answer) / 2)
            new_password.append(answer[:middle_index])

        if len(answer) % 2 == 1:
            last_character = answer[-2:]
            new_password.append(last_character)


    password = ''.join(new_password).title()
    print(new_password)
    print(len(password))
    return password

def glue_string_together(step_two, step_three, step_four):


    if len(step_two) % 2 == 0:
        new_password = f'{step_four}{step_two}{step_three}'
        return f'Your new password is: {new_password}'

    elif len(step_two) % 2 == 1:
        new_password = f'{step_three}{step_two}{step_four}'
        return f'Your new password is: {new_password}'


step_one = generate_a_password()
step_two = create_string(step_one)
step_three = generate_random_numbers()
step_four = generate_random_symbol()

# add step one & two password to the string
step_five = glue_string_together(step_two, step_three, step_four)
print(step_five)