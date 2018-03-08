import sys

# Reads every line and formats into: time, magnitude, degree
def parse_line(linestr):
	try:
		timestr, rest = linestr.split('\t')

		# Find indices of where '(' and ')' occur
		parenst, parenend = (rest.find('(')+1,  rest.find(')'))
		# If they are empty, throw an error
		if (parenst == -1) or (parenend == -1):
			ValueError

		magstr, phastr = rest[parenst:parenend].split(',')
		time = float(timestr) 
		mag = float(magstr.replace('dB', ''))
		deg = float(phastr.replace('°', ''))

		return time, mag, deg
	except ValueError as e:
		return None

# Reads and returns each line in the file
def ltspiceReadAC(fname):
	time, mag, deg = [], [], []
	try:
		with open(fname, 'r') as f:
			for line in f:
				timetmp, magtmp, degtmp = parse_line(line)
				time.append(timetmp), mag.append(magtmp), deg.append(degtmp)
	except OSError as err:
		print("OS error: {0}".format(err))
	
	return time, mag, deg