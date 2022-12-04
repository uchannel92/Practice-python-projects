def when_will_you_turn_onehundred(hundrdyearsofage=100, year=2022):
	""" Function will let you know what year you will turn 100 """

	while True:

		name = input('What is your name?: ')
		age = int(input('What is your age?: '))
		calculate_year_born = year - age
		year_when_100 = calculate_year_born + hundrdyearsofage
		print(year_when_100)

		final_question = input('Is there another person behind? y/n')

		if final_question == 'n':
			break

	return f'{name} {year_when_100}'

when_will_you_turn_onehundred()