from random import choice

attempts = 6
encrypted_word = []
letters_used = []
is_game_over = True

def input_a_letter(letters_used):
    letter = input('Guess your letter: ')
    format_letter = letter.strip()
    if format_letter in letters_used:
        print(f'letter "{format_letter}" has been used!')
        print(letters_used)
    else:
        letters_used.append(format_letter)

    return format_letter

# pull random word from the sowpads.txt file

def get_word_less_than_five_characters():
    word = add_random_word()

    while len(word) > 6:
        word = add_random_word()

    return word

def add_random_word():
    filename = 'sowpads.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        random_line = choice(lines)

    return random_line.lower().strip()
    

# pass random word function here
def encrypt_random_word(random_word, encrypted_word):
    underscore = '_' 

    for letter in random_word:
        encrypted_word.append(underscore)

    return encrypted_word    


# function for guess
def hangman_letter(guess, word, encrypted_word):

    if guess in word:
        print('Correct!')
    else:
        print('Incorrect!')

    for i in range(len(word)):
        if word[i] == guess:
            encrypted_word[i] = guess

    return encrypted_word


def print_list(encrypted_word):
    return ''.join(encrypted_word)

# function to check game is over
def check_if_game_over(user_answer, word ,attempts):
    if user_answer in word:
        return attempts

    elif user_answer not in word:
        print(f'{attempts - 1} guesses left!')
        attempts = attempts - 1
        return attempts

the_random_word = get_word_less_than_five_characters()
word_encryption = encrypt_random_word(the_random_word, encrypted_word)


print('>>> Welcome to Hangman!')
print(f'Word is {len(encrypted_word)} letters')
while is_game_over:

    encrypted_string = print_list(encrypted_word)
    print(encrypted_string)
    print(f'Letters used: {letters_used}')

    if the_random_word == ''.join(encrypted_word):
        print('Winner!')
        print(f'The word was {the_random_word}')
        is_game_over = False

    else:
        user_letter_guess = input_a_letter(letters_used)
        start_game = hangman_letter(user_letter_guess, the_random_word, word_encryption)
        value_check = check_if_game_over(user_letter_guess, the_random_word, attempts)
        attempts = value_check
        if attempts == 0:
            print('Game over!')
            print(f'The word was {the_random_word}')
            is_game_over = False