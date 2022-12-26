def read_file():
	filename = 'categories.txt'

	with open(filename, 'r') as f:
		categories = f.readlines()
	
	return categories



file_request = read_file()


def parse_data(file_request):
	
	formated_lines = []
	for line in file_request:
		formated_line = line.split('/')
		formated_lines.append(formated_line[2])
	
	return formated_lines


def display_categories(formated_lines):

	categories = {}

	for index, category in enumerate(formated_lines):
		categories[category] = formated_lines.count(category)

	return categories


parse_the_data = parse_data(file_request)
display_the_categories = display_categories(parse_the_data)

for key, value in display_the_categories.items():
	print(key, value)

# /a/abbey/sun_aqswjsnjlrfzzhiz.jpg
# /a/abbey/sun_aaoktempcmudsvna.jpg