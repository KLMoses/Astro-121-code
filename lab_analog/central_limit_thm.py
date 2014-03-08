#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import random


empty_list = []

def main():
	sample_size = int(raw_input('Size of Random Sample: '))
	N = int(raw_input('Number of Samples to be Averaged: '))
	plot_normal(N, sample_size)
	raw_input("Press 'Enter' to continue")
	plot_std(N, sample_size)
	raw_input("Press 'Enter' to continue")
	plot_std_vs_N(N, sample_size)


def normal_distribution(N, sample_size):
	random_mean = []
	for x in range (0,N):
		random_list = empty_list[:]                                       
		for y in range(0,sample_size):                                             
			random_list.append(random.randint(1,100))		                    
		random_mean.append(np.mean(random_list))
	return random_mean

def standard_dev(N, sample_size):
	std = np.std(normal_distribution(N, sample_size))
	return std

def plot_normal(N, sample_size):
	a = normal_distribution(N, sample_size)
	plt.title('Central Limit Theorem')
        plt.ylabel('Frequency of Occurence')
        plt.xlabel('Mean')
        plt.hist(a, bins=50)
        plt.show()

def plot_std(N, sample_size):
	x = []
	y = []
	std_list = []
	for m in range(0, sample_size):
		std_list.append(random.randint(1,100))
	for n in [10,50,100,200,300,400,500,600,700,800,900,1000]:
		x.append(n)
		y.append(standard_dev(N, n))
	plt.title('Standard Deviation as a Function of Sample Size')
	plt.ylabel('Standard Deviation')
	plt.xlabel('Sample Size')
	plt.plot(x, np.std(std_list)/(np.sqrt(x)), color = 'g')
	plt.plot(x,y, 'bo')
	plt.show()

def plot_std_vs_N(N,sample_size):
	x= []
	y = []
	std_list = []
	for m in range(0, sample_size):
		std_list.append(random.randint(1,100))
	for n in range(1,500,2):
		x.append(n)
		y.append(standard_dev(n, sample_size))
	plt.title('Standard Deviation Vs. Number of Samples Averaged')
	plt.ylabel('Standard Deviation')
	plt.xlabel('Number of Averaged Samples')
	plt.plot(x,y, 'o')
	plt.show()

if __name__ == '__main__':
	main()
