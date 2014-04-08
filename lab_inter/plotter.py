#!/usr/bin/env python

import sys
import astropy.io.fits as pyfits
import numpy as np
import matplotlib.pyplot as plt

filename = sys.argv[1]

#This code loads the fits file data into lists
with pyfits.open(filename) as f:
    header = f[1].header
    data = f[1].columns
    data[0].array[0]

for key in header.keys():
	print key, header[key]

#This gets the data columns and turns them into arrays
point_error = data[0].array
time_axis = data[1].array
voltage = data[2].array
LST = data[3].array

#This deletes the bad data points due to the satellite dishes rehoming
n = 0
for i in point_error:
	if i == 0:
		voltage = np.delete(voltage, n)
		time_axis = np.delete(time_axis, n)
	else:
		n += 1

#Boxcar averaging on the data
radius = 100
boxcar = np.array([])
n = 0
for i in voltage[radius:-radius]:
	boxcar = np.append(boxcar, np.mean(voltage[n:n + 2*radius]))
	n += 1


#Plotting the data along with the boxcar average
plt.subplot(2, 1, 1)
plt.title('Raw Moon Data with Boxcar Average')
plt.ylabel('Voltage (mV)')		
plt.plot(time_axis, voltage*1e3, 'b')
plt.plot(time_axis[radius:-radius], boxcar*1e3, 'g')


#Subtracts out the boxcar average to center the data at 0 volts
centered = voltage[radius:-radius] - boxcar
ctime = time_axis[radius:-radius]



#Plotting the data centered on 0 volts
plt.subplot(2, 1, 2)
plt.title('Smoothed Data')
plt.ylabel('Voltage (mV)')
plt.xlabel('time (s)')
plt.plot(ctime, centered*1e3, 'b')
plt.show()

#Calculating the fourier transform and power spectrum
fft = np.fft.fft(centered)
pspec = np.abs(fft)**2
freq = np.fft.fftfreq(centered.size)

#Plotting the power spectrum
plt.plot(freq, pspec)
plt.show()
