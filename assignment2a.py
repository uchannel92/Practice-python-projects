# enter a number and the function will convert to a float data type
def convert_input_to_float(my_input):

	format_list = my_input.split(':')[:-1]
	floats = [float(value) for value in format_list]
	print(floats)
	return floats


# add data here
convert_input_to_float()