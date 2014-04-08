#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as plt
import radiolab as rlab

data = np.load('cyg-a.npz')
Y = data['arr_0']
time = data['arr_1']
LST = data['arr_2']*np.pi/180
RA = data['arr_3']*np.pi/180
dec = data['arr_4']*np.pi/180

S = Y.size

ha = LST - RA

#Generates guesses for C
radius = 1
Cmed = 2 * np.pi * 10 * 10.5*1e9/3e8 * np.cos(dec)
C = np.linspace(Cmed - 100, Cmed + 100, 300)
B = C * 3e8 / (2 * np.pi * 10.5e9 * np.cos(dec))


best = [100]
F = np.cos(Cmed * np.sin(ha)) - np.sin(Cmed * np.sin(ha))
S_SQ = np.array([])
for b in B:
	
	X = np.zeros((2, Y.size))
	X[0,:] = np.cos(2 * np.pi * b * 10.5*1e9/3e8 * np.cos(dec) * np.sin(ha)) 
	X[1,:] = np.sin(2 * np.pi * b * 10.5*1e9/3e8 * np.cos(dec) * np.sin(ha))


	XX = np.dot(X,np.transpose(X))
	XY = np.dot(Y,np.transpose(X))
	XXI = np.linalg.inv(XX)
	AB = np.dot(XY,XXI)
	YBAR = np.dot(AB,X)
	DELY = Y - YBAR
	s_sq = np.sum(DELY**2)

	S_SQ = np.append(S_SQ, s_sq)

n = np.where(S_SQ == np.min(S_SQ))


plt.plot(B, S_SQ)
plt.title('Least-squares for Cyg A')
plt.xlabel('Guess for Baseline (m)')
plt.ylabel('wtf')
plt.text(9.5, np.min(S_SQ), 'Best Guess = ' + str(B[n[0][0]]))
plt.show()
