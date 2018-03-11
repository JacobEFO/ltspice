import sys, codecs

# Reads every line and formats into: freq, magnitude, degree
def parse_line(linestr):
	try:
		freqstr, rest = linestr.split('\t')

		# Find indices of where '(' and ')' occur
		parenst, parenend = (rest.find('(')+1,  rest.find(')'))
		# If they are empty, throw an error
		if (parenst == -1) or (parenend == -1):
			ValueError

		magstr, degstr = rest[parenst:parenend].split(',')
		freq = float(freqstr) 
		mag = float(magstr.replace('dB', ''))
		deg = float(degstr.replace('°', ''))

		return freq, mag, deg
	except ValueError as e:
		return None

# Reads and returns each line in the file
def ltspiceReadAC(fname):
	freq, mag, deg = [], [], []
	try:
		with open(fname, 'r', encoding='cp1252') as f:			
			i = 0
			for line in f:
				if i == 0:
					i += 1
				else:
					freqtmp, magtmp, degtmp = parse_line(line)
					freq.append(freqtmp), mag.append(magtmp), deg.append(degtmp)
	except OSError as err:
		print("OS error: {0}".format(err))
	
	return freq, mag, deg