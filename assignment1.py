# Paste values here i.e 12:15:100 etc..
a = input()

# converts string input into a list with a colon after each string.
def convert_input_to_list(my_input):
	
	arr = my_input.split(':')
	print(arr)
	return arr


convert_input_to_list(a)