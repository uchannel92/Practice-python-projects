list_of_values = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def values_less_than_five(list):

	vals_less_than_five = [value for value in list if value < 5]

	return vals_less_than_five

values_request = values_less_than_five(list_of_values)
print(values_request)

def numbers_less_than_request(number):

	numbers_less_than = [value for value in range(int(number))]

	return numbers_less_than


number_request = numbers_less_than_request(input('Enter a number: '))
print(number_request)