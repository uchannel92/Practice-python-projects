# Time for some fake graphics! Let’s say we want to draw game boards that look like this:
#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

horizontal_line = ' ---'
vertical_line = '|   '

def draw_board(grid_dimensions, horizontal_line, vertical_line):

    print('Note: Dimensions over 12 will not be used')
    print('Enter 1 digit i.e. 3x3 grid - enter 3\n')

    if int(grid_dimensions) > 19:
        print('Follow the guideline!')
        return None
    else:
        # how many times the string will be printed
        for box in range(grid_dimensions):
            print(horizontal_line * grid_dimensions)
            print(vertical_line * (grid_dimensions + 1))
        print(horizontal_line * grid_dimensions)
        

# update the first argument to change the dimensions
start_game = draw_board(3, horizontal_line, vertical_line)