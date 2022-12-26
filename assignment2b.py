# Paste values here i.e namn12:ruben12:15:100 etc..
a = input()

def convert_input_to_lists(my_input):

	format_list = my_input.split(':')
	string_list, float_list  = [], []

	for value in format_list:
		try:
			convert_to_float = float(value)
		except ValueError:
			string_list.append(value)
		else:
			float_list.append(convert_to_float)

	print(string_list)
	print(float_list)


convert_input_to_lists(a)