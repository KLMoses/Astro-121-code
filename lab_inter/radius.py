#!/usr/bin/env python

import numpy as np
import matplotlib.pylab as plt
import radiolab as rlab

data = np.load('sunenv.npz')
Y = data['arr_0']
time = data['arr_1']
LST = data['arr_2']*np.pi/180
RA = data['arr_3']*np.pi/180
dec = data['arr_4']*np.pi/180


ha = LST - RA

#Generates guesses for phi
phi = np.linspace(0, np.pi, 2000)


S_SQ = np.array([])
for angle in phi:
	F = np.cos(347.2 * np.cos(dec) * np.cos(ha + 2.2567919212380905))

	X = np.zeros((3, Y.size))
	X[0,:] = F
	X[1,:] = ha * F
	X[2,:] = ha**2 * F

	XX = np.dot(X,np.transpose(X))
	XY = np.dot(Y,np.transpose(X))
	XXI = np.linalg.inv(XX)
	AB = np.dot(XY,XXI)
	YBAR = np.dot(AB,X)
	DELY = Y - YBAR
	s_sq = np.sum(DELY**2)

	S_SQ = np.append(S_SQ, s_sq)

print AB
plt.plot(phi, S_SQ )
plt.plot(time, Y)
plt.plot(time, YBAR)
plt.show()
plt.plot(phi, S_SQ)
plt.show()

