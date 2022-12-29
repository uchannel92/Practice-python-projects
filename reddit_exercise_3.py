
# Create a code that reads in numbers from a user then sort these number in a list from lowest to highest then print 
# out the entire list in order, mean value of all the numbers, smallest number and biggest number, but make the code keep reading in 
# numbers untill the input is X

# assignment 3b: build on the code form the previous assignment (3a) read in numbers untill the input is x and print out the length 
# of the list and then iterate over the entire list and print each value as shown in the example below.

# https://discord.com/channels/@me/1055198213012988016/1056984082204078130

loop_closure_codes = ['x', 'X']
numbers = []

def sort_list(numbers):

	sorted_list =  sorted(numbers)
	list_stats = {
		'smallest_to_largest': sorted_list,
		'mean': format(sum(numbers) / len(numbers), '.2f'),
		'smallest': format(sorted_list[0], '.2f'),
		'largest': format(sorted_list[-1], '.2f'),
	}

	# highest to lowest
	print(f"resultat:{list_stats['smallest_to_largest']}")
	print(f"snitt:{(list_stats['mean'])}")
	print(f"min:{list_stats['smallest']}")
	print(f"max:{list_stats['largest']}")


while True:

	# program starts. Enter a number
	prompt = input()
	
	if prompt in loop_closure_codes:
		break
		
	else:
	    numbers.append(int(prompt))
	    
lowest_to_highest = sort_list(numbers)