# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
# One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

primes = []
happys = []

def read_file(filename, num_array):

	with open(filename, 'r') as f:
		lines = f.readlines()

	for line in lines:
		format_line = int(line.strip())
		num_array.append(format_line)

	return num_array


def overlapped_numbers(list_one, list_two):

	overlapped_numbers = [duplicate for duplicate in list_one if duplicate in list_two]
	return len(overlapped_numbers), overlapped_numbers

prime_numbers = read_file('prime_numbers.txt', primes)
happy_numbers = read_file('happy_numbers.txt', happys)
overlaps = overlapped_numbers(prime_numbers, happy_numbers)
print(overlaps)