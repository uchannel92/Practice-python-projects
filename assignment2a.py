# Paste values here i.e 12:15:100 etc..
a = input()

# enter a number and the function will convert to a float data type
def convert_input_to_float(my_input):

	format_list = my_input.split(':')
	floats = [float(value) for value in format_list]
	print(floats)
	return floats


convert_input_to_float(a)