# Password generator
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
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
        'Enter your name spelt backwards?: ', 'Enter your favourite animal: ' 
    ]

    random_question = choice(questions)

    return random_question


def generate_a_password():

    answers = []
    asked_questions = []

    genrate_question = generate_a_random_question()
    asked_questions.append(genrate_question)

    # first_question = input(genrate_question)
    # answers.append(first_question)

    while len(answers) != 4:

        check_question = generate_a_random_question()

        if check_question in asked_questions:
            # If the random question has already been asked, skip and ask a new question.
            pass
        else:
            # Ask the next unanswered question, and add to password container.
            next_question = input(check_question)
            asked_questions.append(check_question)
            answers.append(next_question)
            # print(asked_questions)

    return answers

test_func = generate_a_password()
print(test_func)