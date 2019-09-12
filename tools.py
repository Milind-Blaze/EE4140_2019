"""This module contains tools and utility functions to complete simulations in the course EE4140.

Author: Milind Kumar Vaddiraju, milind.blaze9@gmail.com
"""

import itertools
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import scipy

def symbol_transmitted_binary(p = 0.5):
	"""Function to determine which of two symbols is transmitted

	Simulates transmission of symbols when only two messages (1 
	or -1) can be transmitted. 
	
	Simulation 1

	Args:
		p (float): probability  of symbol 1 being transmitted,
			defaults to 0.5. The probability of symbol -1 being 
			transmitted is 1 - p. 
	Returns:
		symbol (int): either 1 or -1, whichever symbol is 
		to be transmitted

	"""

	# simulate a coin toss 
	random_value = np.random.random()
	if random_value <= p:
		symbol = 1
	else:
		symbol = -1

	return symbol


def generate_bits(p = 0.5):
	"""Function to generate bits 1 and 0 for transmission

	Very similar to the function above. Generates bits (0 or 
	1) which are likely to be transmitted in a sequence.   

	Simulation 2

	Args:
		p (float): probability  of bit 1 being generated for 
			transmission, defaults to 0.5. The probability 
			of bit 0 being generated for transmission is 
			1 - p. 
	Returns:
		bit (int): either 1 or 0, whichever symbol is 
		to be transmitted

	"""

	# simulate a coin toss 
	random_value = np.random.random()
	if random_value <= p:
		bit = 1
	else:
		bit = 0

	return bit 


def generate_M_QAM_symbol(M):
	"""Select one symbol from a M-QAM constellation for transmission

	There are M symbols (constellation points) of which any 
	one can be transmitted. Each symobol corresponds to one 
	sequence of log2(M) bits. The function generates log2(M)
	bits (0 and 1 have equal probability) independently to 
	generate one symbol which can be transmitted. The decimal 
	value of the point is returned.

	Simulation 2

	Args:
		M (int): number of points in the M-QAM consteallation

	Returns:
		symbol (int): The decimal value of the constellation 
			point generated. For example, if 1100 is generated
			then 12 is returned.
	"""

	# number of bits needed to represent each message
	num_bits = np.log2(M)

	# generate each bit and weight with powers of 2
	symbol = 0
	for position in np.arange(num_bits):
		bit = generate_bits()
		symbol = symbol + bit*(2**position) 

	symbol = int(symbol)

	return symbol


def generate_coordinates_M_QAM(M,d):
	""" Generate a mapping for QAM constellation points

	The coordinates, both X and Y, for M-QAM vary from
	-(root(M) -1)d/2 to (root(M) - 1)d/2. Each symbol 
	varying from 0 to M-1 is mapped to one point.
	
	Simulation 2

	Args:
		M (int): number of points in the M-QAM constellation
		d (float): minimum distance between constellation points

	Returns:
		coordinates (list): a list of coordinates of symbols with 
			ith element corresponding to the coordinates of the ith
			point i.e coordinates[2] is the mapping of the symbol 2 
			or equivalently 0010
	"""

	one_dimension = np.arange(-(np.sqrt(M)-1)*d/2, (np.sqrt(M)-1)*d/2 + d/100, d)

	coordinates = []

	for coordinate in itertools.product(one_dimension, one_dimension):
		coordinates.append(coordinate)

	coordinates = np.array(coordinates)

	return coordinates




def AWGN_transmit(symbol, N0):
	"""Simulates the transmission of a given symbol through a AWGN channel

	Takes in a symbol's coordinates, adds Gaussian noise with 
	power N0/2. The covariance matrix is (N0/2)I

	simulation 2

	Args: 
		symbol (ndarray): a n (2) dimensional symbol to be transmitted
		N0 (float): noise power of the gaussian noise in any one dimension

	Returns:
		transmission (ndarray): a noise transmitted symbol 
	"""

	n_dim = len(symbol)

	noise = np.random.normal(loc = 0, scale = np.sqrt(N0/2), size = n_dim)

	transmission = symbol + noise

	return transmission



def AWGN_ML_detector(mapping, symbol):
	"""Implements ML detector for AWGN channel model

	Declares as transmitted that symbol to which the received symbol 
	is closest. Eucledean norm is used to measure distance.

	Simulation 2

	Args:
		mapping (list): A list in which the ith element corresponds to the 
			ith constellation point. Typically the output of the function
			generate_coordinates_M_QAM.
		symbol (ndarray): output of AWGN channel, a n-dimensional vector 

	Returns:
		prediction (int): the constellation point to which the received 
			symbol is closest. If the distance between mapping[i] and 
			symbol is minimum then prediction = i. 

	"""

	mapping = np.array(mapping)

	prediction = np.argmin(np.sum((mapping - symbol)**2, axis = 1))

	return prediction







