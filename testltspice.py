import ltspice
import random

def gen_data():
	freq = random.randint(0,100)*1e6
	db = random.lognormvariate(2,0.5)
	phase = random.uniform(0,360)
	truncate = lambda x: float('{:.15e}'.format(x))
	return truncate(freq), truncate(db), truncate(phase)

def format_data_line(datap1):
	freq, db, degree = datap1[0], datap1[1], datap1[2]
	formatted = "{0:.15e}\t({1:.15e}dB,{2:.15e}°)\n"
	return formatted.format(freq, db, degree)

def create_test_file(fname, lines):
	data = ""
	for line in range(lines):
		data += format_data_line(gen_data())

	with open(fname, 'w') as f:
		f.write(data)
	return

def setupTestEnv(fname):
	lns = 10 # number of lines in test file
	create_test_file(fname, lns)

# Test error handling when looking up file
def testFileError():
	freq, mag, deg = ltspice.ltspiceReadAC("foobar.txt")

# Tests error handling for .txt syntax
def testTabError():
	pass

def testParsing(fname):
	freq, mag, deg = ltspice.ltspiceReadAC(fname)
	print(freq)
	print(mag)
	print(deg)


if __name__ == '__main__':
	fname = "test.txt"
	setupTestEnv(fname) # create test
	testParsing(fname)
	
	# Test file errors/handling
	testFileError()
	# testTabError() # Include this once function has been made
