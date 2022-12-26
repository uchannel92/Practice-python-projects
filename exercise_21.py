# Make a smaller number range 10
# Starr for loop name prime_check in numbers
# Change number check condition to prime_check
# Change break to pass in for loop
# Change function argument to number list

filename = 'primes.txt'
filename_two = 'happy.txt'

numbers = list(range(1,1001))
primes = []

def is_number_prime_optimised(numbers, primes):

    for is_prime in numbers:

        result = True
        for number in range(2, is_prime):
            if is_prime % number == 0:
                result = False
                pass
       
        if result:
            primes.append(is_prime)
    print(primes)



def is_number_happy_number():
    pass


prime_number_check = is_number_prime_optimised(numbers[1:], primes)

with open(filename, 'a') as f:
    for prime_num in primes:
        f.write(f'{str(prime_num)}')
        f.write('\n')

# A happy number is defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process 
# until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
# Write a Python program to check whether a number is "happy" or not.


# STEP 1: isHappyNumber() determines whether a given number is happy or not.
# If the number is greater than 0, then calculate remainder rem by dividing the number with 10.

# Calculate square of rem and add it to a variable sum.
# Divide number by 10.
# Repeat the steps from a to c till the sum of the square of all digits present in number has been calculated.
# Finally, return the sum.
# STEP 2: Define and initialize variable num.
# STEP 3: Define a variable result and initialize it with a value of num.
# STEP 4: If the result is neither equal to 1 nor 4 then, make a call to isHappyNumber().
# STEP 5: Otherwise, if the result is equal to 1 then, given number is a happy number.
# STEP 6: If the result is equal to 4 then, given number is not a happy number.