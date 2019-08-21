"""This module contains tools and utility functions to complete simulations in the course EE4140.

Author: Milind Kumar Vaddiraju, milind.blaze9@gmail.com
"""

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import scipy

def symbol_transmitted_binary(p = 0.5):
	"""Function to determine which of two symbols is transmitted

	Simulates transmission of symbols when only two messages (1 
	or -1) can be transmitted. 

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