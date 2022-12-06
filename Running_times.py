filename = 'runners.txt'

with open(filename, 'r') as f:
	running_data = f.readlines()

#print(running_data)
runners = []

for runner_data in running_data:
	
	split = runner_data.split()

	# build a dict for each runner
	athlete = {
		'fullname': split[:2],
		'times': split[2:],
	}

	runners.append(athlete)

runners.pop(0)
for athlete in runners:
	firstname = athlete['fullname'][0]
	lasttname = athlete['fullname'][1]
	name = f'{firstname} {lasttname}'

	athlete_times = athlete['times']
	times = [float(time) for time in athlete_times]	
	average_time = sum(times) / len(times)
	sorted_times = sorted(times, reverse=True)
	fastest_time = sorted_times[0]
	slowest_time = sorted_times[-1]
	
	print(f'Name: {name}')
	print(f'Fastest time: {fastest_time}')
	print(f'Slowest time: {slowest_time}')
	print(f'Average split: {round(average_time, 2)}')
	print(f'All time splits: {sorted_times}\n')




# assignment:

# (we are given a txt file with 20 participants going for a run with 10 different runs each)

# Read data from the file for each participant and then split this data so that it is saved in a list (Hint: Use the built-in function split( )). In the first and second positions print the names and followed by positions with results from the file

# For each participant; find out: a. the best time. b. the worst time c. the mean value of the ten results

# For each participant; sort the times so that the best time is first and the worst last.

# Print on the screen (for each participant, incl. appropriate prompt text): a. On row 1: names and times sorted from best to worst b. On line 2: "best time", "best time" and "average_of_the_times". c. Blank line between participants, i.e. the third line becomes a blank line