def when_will_you_turn_onehundred(name, age, hundrdyearsofage=100, year=2022):
	""" Function will let you know how many years when
		you will turn 100
	"""

	calculate_year_born = year - age
	year_when_100 = calculate_year_born + hundrdyearsofage

	answer = f'Hello {name}, you are {age}.\nYou will be 100 in the year {year_when_100}!'

	return year_when_100

my_answer = when_will_you_turn_onehundred('uchenna', 5)
# print(my_answer)

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.
