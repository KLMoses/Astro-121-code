#!/usr/bin/env python

import radiolab as rlab
import pylab as plt
import numpy as np

N = 256
f_sample = 1000000.

x = np.arange(256)/f_sample*1e6
data = []

for i in range(1,10):
        y = np.load('data'+str(i)+'.npz')
        ET = y['arr_0']
        EF = np.fft.fft(ET)
	PF = np.abs(EF)**2
	data.append(PF)

freq = np.fft.fftfreq(N, 1e3 * 1/f_sample)

for i in range (1,10):
        plt.subplot(3,3,i)
        if i == 2:
                plt.title("Power Spectrum" + '('+r'$\nu_{sample} = 1MHz$)' + '\n' + r'$\nu_{sig} = $'+str(i)+'00 kHz', fontsize =18)
	else:
		plt.title(r'$\nu_{sig} = $'+str(i)+'00 kHz')
        if i == 4:
                plt.ylabel('power (kW)')
        if i == 8:
                plt.xlabel('frequency (kHz)')
	if i == 1 or i == 4 or i == 6 or i == 9:
		plt.ylim(0, 10)
	if i == 2 or i == 3 or i == 7 or i == 8:
		plt.ylim(0, 15)
        plt.plot(freq, data[i-1]*1.0e-3)

plt.show()  
