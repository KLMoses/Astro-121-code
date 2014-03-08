#!/usr/bin/env python

import numpy as np
import radiolab as rlab
import pylab as plt


x1 = np.array([1.,1.,1.,0.,0.,0.,1.,1.])
f = np.array([0.,25.,50.,75.,-100.,-75.,-50.,-25.])
t = np.array([0.,5.,10.,15.,20.,25.,30.,35.])

y = np.fft.ifft(x1)
y1 = np.fft.fftshift(y)

zero = np.arange(56)*0.0
y2 = np.concatenate((y1,zero))


x = np.fft.fft(y2)
x2 = abs(x)**2
freq = np.arange(-100,100,3.125)

plt.subplot(2,1,1)
plt.axvline(x=-62.5, ymin = .1/1.6, ymax= 1.1/1.6,color = 'k')
plt.axvline(x=62.5, ymin = .1/1.6, ymax = 1.1/1.6,color = 'k')
plt.axhline(y=0,xmin= 0,xmax= 7./24,color = 'k')
plt.axhline(y=0,xmin= 17./24,xmax = 1,color = 'k')
plt.axhline(y=1,xmin= 7./24,xmax= 17./24, color = 'k')
plt.plot(f,x1, 'g^')
plt.plot(freq,np.fft.ifftshift(x2),'g--')
plt.ylim(-.1, 1.5)
plt.xlim(-150,150)
plt.xlabel('frequency (MHz)')
plt.ylabel('filter response')

plt.subplot(2,1,2)
plt.plot(t,y1, 'g^')
plt.xlim(0,40)
plt.xlabel('time (ns)')
plt.ylabel('coefficient value')
plt.show()
