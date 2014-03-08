#!/usr/bin/env python

import radiolab as rlab
import pylab as plt
import numpy as np

N = 256
f_sample = 1000000.

x = np.arange(256)/f_sample*1e6
data = []
x_2 = np.arange(0,256,.01)
sin = np.sin(x_2*np.pi*2)


for i in range(1,10):
	y = np.load('data'+str(i)+'.npz')
	ET = y['arr_0']
	data.append(ET)

for i in range (1,10):
	plt.subplot(3,3,i)
	if i == 2:
		plt.title("Waveform Sampling " + '('+r'$\nu_{sample} = 1MHz$)' + '\n\n', fontsize =18)
	if i == 4:
		plt.ylabel('amplitude (V)')
	if i == 8:
		plt.xlabel('time $\mu$s')
	plt.text(7, 1.1, r'$\nu_{sig} = 0.$'+str(i)+r'$MHz$',fontsize =14)
	plt.xlim(0,20)
	plt.ylim(-1.1,1.5)

	if i == 1:
		plt.plot(x_2/(.1*i)-10.2,sin, color ='0.7',lw = 5.)
	if i == 2:
		plt.plot(x_2/(.1*i),sin, color ='0.7',lw = 5.)
	if i == 3:
		plt.plot(x_2/(.1*i)-2.55,sin, color ='0.7',lw = 5.)
	if i == 4:
		plt.plot(x_2/(.1*i)-0.32,sin, color ='0.7',lw = 5.)
	if i == 5:
		plt.plot(x_2/(.1*i)-0.5,sin, color ='0.7',lw = 5.)
	if i == 6:
		plt.plot(x_2/(.1*i)-1.35,sin, color ='0.7',lw = 5.)
	if i == 7:
		plt.plot(x_2/(.1*i)-0.83,sin, color ='0.7',lw = 5.)
	if i == 8:
		plt.plot(x_2/(.1*i)-.38,sin, color ='0.7',lw = 5.)
	if i == 9:
		plt.plot(x_2/(.1*i)-.75,sin, color ='0.7',lw = 5.)
	plt.plot(x, data[i-1], x, data[i-1], 'bo')

plt.show()
