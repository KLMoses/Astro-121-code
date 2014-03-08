#!/usr/bin/env python

import radiolab as rlab
import pylab as plt
import numpy as np

N = 8192
f_sample = 10000000.
x=np.arange(N)*1e6/f_sample   #sets scale of time axis

y_1 = np.load('pulsar_mixing.npz')
ET_1 = y_1['arr_0']
y_2 = np.load('pulsar_mixing2.npz')
ET_2 = y_2['arr_0']

'''
plots the sampled signal vs time
'''
"""
plt.subplot(121)
plt.plot(x,ET_1, '#386cb0')
plt.title ('Digitally Sampled Mixed Signal' + '\n' + '($f_{sig} =$' + ' 295 $kHz$;' +  ' $f_{lo}=$' + '300 $kHz$)')
plt.ylabel('amplitude (V)')
plt.xlabel('time ($\mu$s)')
plt.ylim(-1.1, 1.1)

plt.subplot(122)
plt.plot(x, ET_2, '#fdc086')
plt.title ('Digitally Sampled Mixed Signal' + '\n' + '($f_{sig} =$' + ' 305 $kHz$;' +  ' $f_{lo}=$' + '300 $kHz$)')
plt.xlabel('time ($\mu$s)')
plt.ylim(-1.1, 1.1)
plt.show()
"""

EF_1 = np.fft.fft(ET_1)                        #fourier transforms sampled signal
PF_1 = np.abs(EF_1)**2
EF_2 = np.fft.fft(ET_2)
PF_2 = np.abs(EF_2)**2

freq = np.fft.fftfreq(N, 1e3 * 1/f_sample) #sets the scale of frequency axis


'''
plots fourier transform of sampled signal
'''

plt.plot(freq, PF_1,'#386cb0', lw= 4.0)
plt.plot(freq, PF_2*3.8,'#fdc086', lw = 3.0)
plt.title('Power Spectrum')
plt.xlabel('frequency (kHz)')
plt.ylabel('power (W)')
plt.xlim(-700,700)
plt.ylim(0)
plt.show()
