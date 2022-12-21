from random import randint

list_one = [3, 5, 1, 6]
computer = [3, 5, 2, 6]

random_numbers = str(randint(1000,9999))
random_numbers_list = [int(value) for value in random_numbers]


attempts = 0

while True:
	cow_count = 0
	bull_count = 0
	user_guess = input('enter a 4 digit number: ')
	user_guess_list = [int(value) for value in user_guess]
	print(f'Your list: {user_guess_list}')

	for index, item in enumerate(zip(user_guess_list, random_numbers_list)):

		if user_guess_list[index] == random_numbers_list[index]:
			cow_count += 1

		elif user_guess_list[index] != random_numbers_list[index] and user_guess_list[index] in random_numbers_list:
			bull_count += 1


	print(f'cow {cow_count}, bull {bull_count}')
	attempts += 1
	
	if user_guess_list == random_numbers_list:
		print(f'SUCCESS! {attempts} attempts')
		print(f'Your list: {user_guess_list}')
		print(f'CPU  list: {random_numbers_list}')
		break

	