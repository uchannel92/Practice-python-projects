dash, line  = '|', '-'
top, sides, empty_space = '', '', ' '
nums = [0, 4, 8, 12]

for num in range(13):

    if num in nums:
        top += dash
        sides += empty_space
    else:
        top += empty_space
        sides += line


for num in range(7):
    if num % 2 == 0:
        print(sides)
    else:
        print(top)