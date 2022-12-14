# function that reads all data from a file
# as an input parameter, a file name to an existing file needs to be specified
# the function returns all data from file with specified filename as a text string
def read_file(filename):
    """ Read conents of the file. """

    athletes_and_times = []
    with open(filename, 'r') as f:
        all_athlete_info = f.readlines()

        for line in all_athlete_info:
            stripped_line = line.rstrip()
            athletes_and_times.append(stripped_line)
   
    return athletes_and_times


# Obtain the values for each athlete
# Loop through the athletes list
# format the data into a neat string.
# append formatted data to new list.
def get_max_min_avg(athletes_list):
    """ Return the min max and mean number values to a dict """
   
    athletes = []
   
    for line in athletes_list:
        split = line.split()
        firstname = split[0]
        lasttname = split[1]
        fullname = f'{firstname} {lasttname}'
        times = [float(time) for time in split[2:]]
        sorted_times = sorted(times, reverse=True)
        max = sorted_times[0]
        min = sorted_times[-1]
        avg = sum(times) / len(times)

        string = f'Name: {fullname}\nTimes: {sorted_times}\nMax: {max}\nMin: {min}\nAverage: {round(avg, 2)}\n'
        athletes.append(string)

    return athletes
   

# function to write data to a text file.
# each line in the formatted list with be appened to the new text file.
def write_file(formatted_list, new_filename):

    with open(new_filename, 'a') as f:
        for line in formatted_list:
            f.write(line)
            f.write('\n')


# function to process the data.
# Enter the filename and the special character to load the file.
# I've hard coded the file names in your spec. So what you want to do is maybe
# change filename and newfilename into 'inputs' so you can manually type the filenames your lecturer has asked. 
def process_data():
   
    while True:
        # enter the filename you want processed, then prompted to conifirm the New filename.
        prompt = input('Enter any key to continue or enter "X" to exit: ')

        if prompt == 'X':
            break

        else:

            filename = input('Enter the filename to process: ')
            new_filename = input('Enter the processed filename: ')
           
            # Declare as a variable, and then return that value.
            if filename:
                athletes_list = read_file(filename)
                formatted_list = get_max_min_avg(athletes_list)
                write_file(formatted_list, new_filename)
                continue

        
   
process_data()
