# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,and print out the results 
# to the screen. I have a .txt file for you, if you want to use it!

filename = 'names.txt'

def read_file(filename):
	""" reads file and returns output. """
	names = []

	with open(filename, "r") as f:
		unformatted_list = f.readlines()

		for line in unformatted_list:
			formated_line = line.strip()
			names.append(formated_line)

	return names


def display_names(names):
	""" List all names from list into a dictionary """

	names_dict = {}

	for index, name in enumerate(names):
		names_dict[name] = names.count(name)

	return names_dict


if __name__ == '__main__':
	read_text_file = read_file(filename)
	list_names = display_names(read_text_file)
	print(list_names)