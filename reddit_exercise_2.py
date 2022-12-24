# Test strings to use
# test_1 = '5:2:4'
# test_2 = '5:100:24'
# test_3 = '5:100:24:13:70'
# test_4 = 'namn1:namn2:4:2:3'
# test_5 = 'a:b:9:8:6:5'


# Function determines the number of elements that will be added to a list.
def input_counter():

    
    prompt = """\nSelect the option (1/2/3) to deterime the number of inputs you require (This determines list length):\n1) Small (3)\n2) Medium (6)\n3) Large (8)\n: """
    question = input(prompt)
    list_length, string = '', ''
    
    if question == '1':
        list_length = 3
    elif question == '2':
        list_length = 6
    elif question == '3':
        list_length = 8
        
    for inputs in range(list_length):
        question_2 = input('add an input: ')
        string = string + question_2 + ':'
        
    return string


# converts string input into a list with a colon after each string.
def convert_input_to_list(my_input):

	 print(my_input.split(':')[:-1])


# enter a number and the function will convert to a float data type
def convert_input_to_float(my_input):

	format_list = my_input.split(':')[:-1]
	floats = [float(value) for value in format_list]
	print(floats)


# splits strings to 2 separate lists - a string and float list.
def convert_input_to_lists(my_input):

	format_list = my_input.split(':')[:-1]
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


# To determine which function runs, select from the following options prompted by the question.
def process_data():

	prompt = input('Select the assignment you want to test:\n1) Convert to list\n2) Convert to float\n3) Convert to float and string: ')


	if prompt == '1':
		my_input = input_counter()
		convert_input_to_list(my_input)

	elif prompt == '2':
		my_input = input_counter()
		convert_input_to_float(my_input)

	elif prompt == '3':
		my_input = input_counter()
		convert_input_to_lists(my_input)

	else:
		print('You have not selected a valid option')

process_data()