# write a program that asks the user for an exam result and prints which grade the results responds to.
# 5th is given if the results is between 50 - 60 points.
# 4th is given if the results is between 40 - 49 points.
# 3rd is given if the results is between 30 - 39 points.
# U is given If the result is below 30 points
# if the user enters a score greater than 60 or less than 0, the text 'invalid result' should be printed on screen
# The program should loop until a user inputs x so if i input 44, the program should output 4 and then keep going until
# input is x

print('Enter your exam result below: ')
def enter_exam_result(user_input):
	""" 
		Enter a number to the exam result.This will return a numerical value.
		If the value cannot be determined, None will be returned.
	"""
	try:
		convert_to_int = int(user_input)
	except Exception as ValueError:
		print('Your input cannot be determined to be a numerical value..')
		return None
	else:
		return convert_to_int


def get_grade(exam_result):
	""" 
		The exam_result paramter is evaluated to represent a grade based on the exam result.
		If the value is not within the below parameters, an error message variable is used.
	"""
	error_message = 'Ogiligt resultat'
	third, fourth, fifth = 3, 4, 5
	fail = 'U'

	if exam_result == None:
		print('We cannot give you a grade.')

	else:
		if exam_result < 0 or exam_result > 60:
			print(error_message)

		elif exam_result < 30:
			print(fail)

		elif exam_result >= 30 and exam_result < 40:
			print(third)

		elif exam_result >= 40 and exam_result < 50:
			print(fourth)

		elif exam_result >= 50 and exam_result < 60:
			print(fifth)

		else:
			print(f'{exam_result} within the params to be tested.')


if __name__ == '__main__':

	while True:

		# program starts. Enter a number

		user_input = input()
		
		if user_input == 'x':
			break
			
		else:
		    exam_result = enter_exam_result(user_input)
		    find_your_grade = get_grade(exam_result)
		    
	print('Done')