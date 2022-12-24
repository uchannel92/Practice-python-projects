# converts string input into a list with a colon after each string.
def convert_input_to_list(my_input):
	
	arr = my_input.split(':')
	print(arr)
	return arr



convert_input_to_list('5:100:24')