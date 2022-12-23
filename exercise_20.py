# Write a function that takes an ordered list of numbers (a list where the elements are in order 
# from smallest to largest) and another number. The function decides whether or not the given number 
# is inside the list and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

def ask_number():

	question = input('Enter a number please: ')
	return int(question)


def is_number_in_list(number):

	one_to_thousand = list(range(1,1001))

	if number in one_to_thousand:
		return True
	else:
		return False


if __name__ == '__main__':
	number = ask_number()
	the_answer = is_number_in_list(number)
	print(the_answer)
	main()