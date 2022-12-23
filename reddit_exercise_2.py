# "Read in a string containing a number of numbers separated by colons (:). 
# Split the character string at each colon character and put each part into a common list. 
# Feel free to use 'split()' for this. Then print this list."

# Test strings to use
test = '5:2:4'
test_2 = '5:100:24'
test_3 = '5:100:24:13:70'
string_int = 'namn1:namn2:4:2:3'
string_int_2 = 'a:b:9:8:6:5'

def convert_input_to_list(my_input):

	 print(my_input.split(':'))


input_test = convert_input_to_list(test)
input_test_2 = convert_input_to_list(test_2)
print('\n')

# "Read in a string containing a number of numbers separated by colons (:). 
# Split the character string at each colon character and put each part into a common list. 
# Convert each element of the list to a floating point number. Then print this list."

def convert_input_to_float(my_input):

	format_list = my_input.split(':')
	floats = [int(value) for value in format_list]
	print(floats)


float_conversion_test = convert_input_to_float(test)
float_conversion_test_2 = convert_input_to_float(test_3)
print('\n')

# Build on the code from the previous task. Read in a string. 
# Break this up at each colon character and add each part to a list. 
# Pick out the first two elements in the list in a separate list, and pick out the remaining elements in another list. 
# Convert all elements of the latter list to floating-point numbers and print both lists on a separate line."

def convert_input_to_lists(my_input):

	format_list = my_input.split(':')
	string_list, float_list  = [], []

	for index, value in enumerate(format_list):
		
		if index > 1:
			convert_to_float = float(value)
			float_list.append(convert_to_float)
		else:
			convert_to_str = str(value)
			string_list.append(convert_to_str)

	print(string_list)
	print(float_list)
	print('\n')


string_int_test = convert_input_to_lists(string_int)
string_int_test_2 = convert_input_to_lists(string_int_2)

