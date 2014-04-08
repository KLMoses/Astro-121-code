#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as plt
import radiolab as rlab

data = np.load('sun.npz')
Y = data['arr_0']
time = data['arr_1']
LST = data['arr_2']
RA = data['arr_3']
dec = data['arr_4']


top = Y
n = 0
for val in top:
	if val < 0:
		top[n] = 0
	n +=1

n = 0
max_n = 0
max_val = 0
envelope = np.array([])
etime = np.array([])
eLST = np.array([])
eRA = np.array([])
edec = np.array([])
for val in top:
	if val > max_val:
		max_val = val
		max_n = n
	if val == 0:
		if top[n-1] != 0:
			envelope = np.append(envelope, max_val)
			etime = np.append(etime, time[max_n])
			eLST = np.append(eLST, LST[max_n])
			eRA = np.append(eRA, RA[max_n])
			edec = np.append(edec, dec[max_n])
			max_val = 0
	n += 1	


radius = 6
boxcar = np.array([])
n = 0
for i in envelope[radius:-radius]:
        boxcar = np.append(boxcar, np.mean(envelope[n:n + 2*radius]))
        n += 1



plt.plot(time, top*1e3)
plt.plot(etime[radius:-radius], boxcar*1e3, '000000')
plt.title("'Zero' Crossing of Sun's Fringe Response")
plt.ylabel('Voltage (mV)')
plt.xlabel('Seconds')
plt.show()
