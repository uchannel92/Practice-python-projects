import math

happy = []

def happy_number(number, happy):
    
    previous_numbers = set()

    while number != 1:
        current = 0
        while number > 0:
            current += (number % 10) * (number % 10)
            number = math.floor(number / 10 )
            
        if number not in previous_numbers:
            previous_numbers.add(number)
            number = current

        else:
            return False

    happy.append(number)
    print(happy)
    return True


print(happy_number(12, happy))