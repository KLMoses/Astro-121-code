#!/usr/bin/env python

import numpy as np
import radiolab as rlab
import ephem, time


tlat = 37.8732 * np.pi / 180                 #Sets terrestrial latitude
tlong = -122.2573 * np.pi / 180              #Sets terrestrial longitude
LST = rlab.getLST()*np.pi/12                 #Sets Local Sidereal Time
sun_ra = rlab.sunPos()[0] * np.pi/12         #Right ascension of the Sun
sun_dec = rlab.sunPos()[1] * np.pi/12        #Declination of the Sun


#Converts coordinate system to Rectangular
def rectanglize(longitude, latitude):
	return np.array([
		np.cos(latitude) * np.cos(longitude),
		np.cos(latitude) * np.sin(longitude),
		np.sin(latitude)
	])

#Converts coordinates to spherical
def sphericalize(xp):
        x = np.arctan2(xp[1], xp[0]) 
        y = np.arcsin(xp[2])
        while x < 0.:
                x += 2 * np.pi
        return x, y



#Converts (RA, DEC) to (HA, DEC)
R_1 = np.array([[np.cos(LST), np.sin(LST), 0],
	[np.sin(LST), -np.cos(LST), 0],
	[0, 0, 1]
])


#Converts (HA, DEC) to (AZ, ALT)
R_2 = np.array([
	[-np.sin(tlat), 0, np.cos(tlat)],
	[0, -1, 0],
	[np.cos(tlat), 0, np.sin(tlat)]
])



def azalt(ra, dec):
	"""Converts Right Ascension, Declination to Azimuth, Altitude

	Inputs: ra = right ascension  (radians)
		dec = declination     (radians)

	Output: Azimuth, Altitude     (radians)"""
	x = rectanglize(ra, dec)
	y = np.dot(R_1, x)
	z = np.dot(R_2, y)
	return sphericalize(z)



#Checking the Rotation Matrices
obs = ephem.Observer()
obs.lat = 37.8732 * np.pi / 180
obs.long = -122.2573 * np.pi / 180
obs.date = ephem.now()

sun = ephem.Sun()
sun.compute(obs)
print float(sun.az), float(sun.alt)
