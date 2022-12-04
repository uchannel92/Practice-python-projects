def when_will_you_turn_onehundred(name, age, hundrdyearsofage=100, year=2022):
	""" Function will let you know what year you will turn 100 """

	calculate_year_born = year - age
	year_when_100 = calculate_year_born + hundrdyearsofage

	answer = f'Hello {name}, you are {age}.\nYou will be 100 in the year {year_when_100}!'
	print(answer)
	print(year_when_100)
	return year_when_100


while True:	

	question_name = input('What is your name? : ')
	question_age = int(input('What is your age?: '))

	my_answer = when_will_you_turn_onehundred(
		question_name, 
		question_age
	)

	final_question = input('Is there another person behind? y/n')

	if final_question == 'n':
		break
