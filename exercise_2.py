def is_odd_or_even():

	number_request = int(input('Enter a number please :) : '))

	if number_request % 4 == 0 and number_request % 2 == 0:
		print('divisible by 4')
		print('also even')

	elif number_request % 2 == 0:
		print('even')

	elif number_request % 2 == 1:
		print('odd')

is_odd_or_even()