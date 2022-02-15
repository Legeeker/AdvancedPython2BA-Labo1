from math import sqrt 
from scipy.integrate import quad    
import numpy as np


def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n == 0 : 
		return 1 
	elif n < 0 : 
		print("erreur")
	else: 
		# F = 1 
		# for k in range(2 , n+1 ):
		# 	F = F * k


		return n * fact(n-1)

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	# a*x^2 + b*x + x == 0 
	inter = b**2 - 4*a*c 
	if inter < 0 : 
		x = tuple()
	elif inter == 0 :  
		x = ((-b)/2*a,)
	else : 
		x = (-b + sqrt(inter))/2*a, -b -sqrt(inter)/2*a   #renvoye des tuples 


	return x 


def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	return quad(lambda x: eval(function), lower , upper)[0]


 
if __name__ == '__main__':
	print(fact(-5))
	print(roots(1, 1, -1))
	print(integrate('x ** 2 - 1', -1, 1))
