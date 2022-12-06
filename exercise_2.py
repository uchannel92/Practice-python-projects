def is_odd_or_even(number):


	if number % 4 == 0 and number % 2 == 0:
		return 'divisible by four, and also even'

	elif number % 2 == 0 and number % 4 != 0:
		return 'even'

	elif number % 2 == 1:
		return 'odd'

num_check = is_odd_or_even(40)
print(num_check)

def is_odd_or_even_dbl_input(input_one, input_two):

	num = input_one
	check = input_two
	result = num / check

	if result % 2 == 0:
		return 'even'
	else:
		return 'odd'


#is_odd_or_even_dbl_input(8, 2)
