"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
	if n == 1:
		return n
	else:
		return a*simple_work_calc(n//b,a,b)+n

def work_calc(n, a, b, f):
	"""Compute the value of the recurrence $W(n) = aW(n/b) + f(n)

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
	if(n==1): #base case
		return n
	else:
		return a*work_calc(n//b,a,b,f)+f(n)

def span_calc(n, step, a, func):
	if n <= 1:  # Base case
			return func(n)

	# Compute the span recursively 
	recursive_span = span_calc(n // step, step, a, func)

	# Compute the total span from the work and the span of the recursive call combined 
	return max(func(n), recursive_span)





def compare_work(work_fn1, work_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different recurrences for given input sizes.

	Returns:
	A list of tuples of the form (n, work_fn1(n), work_fn2(n))
	"""
	result=[]
	for n in sizes:
		result.append((n,work_fn1(n),work_fn2(n)))
	return result


def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'W_1', 'W_2'],
							floatfmt=".3f",
							tablefmt="github"))



def compare_span(span_fn1, span_fn2, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
	"""
	Compare the values of different span recurrences for given input sizes.

	Returns:
	A list of tuples of the form
	(n, span_fn1(n), span_fn2(n), ...)
	"""
	result = []
	for n in sizes:
			result.append((
					n,
					span_fn1(n),  # Call the function with n
					span_fn2(n)   # Call the function with n
			))
	return result
	

