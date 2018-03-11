import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import ltspice
import numpy as np
import matplotlib.pyplot as plt

def tf(s):
	R = 1*10**3
	C = 47*10**-6
	return 1/(1 + R * C * s)

if __name__ == '__main__':
	# Fetch data from exported .txt file
	fname = "lowpassRC.txt"
	freq, mag, deg = ltspice.ltspiceReadAC(fname)

	llimit = np.log10(1) # 1 Hz from LTspice
	hlimit = np.log10(100*10**3) # 100 kHz from LTspice
	f = np.logspace(llimit , hlimit , num=1000)
	H = tf(1j * 2 * np.pi * f)

	# Magnitude
	plt.figure(1)
	plt.semilogx(f, 20*np.log10(np.abs(H)), color = 'black', linewidth=2, label='Calculated')
	plt.plot(freq, mag, color = 'red', linestyle=':', linewidth=2, label='Simulated')
	plt.ylabel('Gain / dB')
	plt.xlabel('Frequency / Hz')
	plt.legend()
	plt.grid()
	plt.show()

	# Phase
	plt.figure(2)
	plt.semilogx(f, np.angle(H)*180/np.pi, color = 'black', linewidth=2, label='Calculated')
	plt.plot(freq, deg, color = 'red', linestyle=':', linewidth=2, label='Simulated')
	plt.ylabel('Phase / $\degree$')
	plt.xlabel('Frequency / Hz')
	plt.grid()
	plt.show()