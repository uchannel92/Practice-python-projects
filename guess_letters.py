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


def add_random_word(word):
    return word.lower()


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
    return ' '.join(encrypted_word)


the_random_word = add_random_word('plum')
word_encryption = encrypt_random_word(the_random_word, encrypted_word)


print('>>> Welcome to Hangman!')
while is_game_over:

    encrypted_string = print_list(encrypted_word)
    print(encrypted_string)

    if the_random_word == ''.join(encrypted_word):
        print('Game over')
        is_game_over = False

    else:
        user_letter_guess = input_a_letter(letters_used)
        start_game = hangman_letter(user_letter_guess, the_random_word, word_encryption)

    