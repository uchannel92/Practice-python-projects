word = 'uchenna'
hashed_word = []


for letter in word:
hash = '_'
hashed_word.append(hash)
print(hashed_word)
string = ''.join(hashed_word)


guess = 'n'
used_letters = ['c']


if guess in used_letters:
	print('Already used')


for i in range(len(word)):
	if word[i] == guess:
		hashed_word[i] = guess
		string = ' '.join(hashed_word)
		print(i)
	else:
		print(guess, 'not here')


print(string)

# guess = 'l'
# word = 'alphabet'
# hangman = []

# for key in word:
#     hangman.append('_')
# print(hangman)

# for index, letter in enumerate(word):
    
#     if guess == letter:
#         print(index, letter)
#         hangman[index] = letter

# print(hangman)


# function for guess