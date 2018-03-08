import random

def gen_data():
	time = random.randint(0,100)*1e6
	db = random.lognormvariate(2,0.5)
	phase = random.uniform(0,360)
	truncate = lambda x: float('{:.15e}'.format(x))
	return truncate(time), truncate(db), truncate(phase)

def format_data_line(datap1):
	time, db, degree = datap1[0], datap1[1], datap1[2]
	formatted = "{0:.15e}\t({1:.15e}db, {2:.15e}°)\n"
	return formatted.format(time, db, degree)

def create_test_file(fname, lines):
	header = "Time Gain Degree"
	data = ""
	for line in range(lines):
		data += format_data_line(gen_data())

	with open(fname, 'w') as f:
		f.write(data)
	return


if __name__ == '__main__':
	lns = 10 # number of lines in test_file
	fname = "test.txt"
	create_test_file(fname, lns)