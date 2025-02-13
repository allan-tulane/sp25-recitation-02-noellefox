from main import *
import math

def test_simple_work():
	""" done. """


	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	assert simple_work_calc(20, 3, 4) == 44
	assert simple_work_calc(35, 2, 3) == 77
	assert simple_work_calc(15, 3, 2) == 90


def test_work():
	#testing multiple cases for questoin 4 to prove derived asymptotic behavior
	assert work_calc(8, 2, 2, lambda n: 1) == 15
	assert work_calc(16, 2, 2, lambda n: 1) == 31

	assert work_calc(8, 2, 2, lambda n: math.log(n, 2)) == 19
	assert work_calc(16, 2, 2, lambda n: math.log(n, 2)) == 42

	assert work_calc(8, 2, 2, lambda n: n) == 32
	assert work_calc(16, 2, 2, lambda n: n) == 80

	#remaining original tests in addittion to our added ones
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	assert work_calc(20, 3, 4, lambda n: n*2) == 79
	assert work_calc(50, 1, 2, lambda n: n+3) == 112
	assert work_calc(10, 1, 2, lambda n: (n+2) * 2) == 47


def test_compare_work():
	sizes = [10, 20, 50, 100, 500, 1000, 5000, 10000]

	# Case 1: c < log_b a (Recursion dominates)
	def work_fn_case1(n):
			a, b, c = 4, 2, 1  # log_2(4) = 2, c < 2
			return work_calc(n, a, b, lambda n: n**c)

	# Case 2: c > log_b a (Work function dominates)
	def work_fn_case2(n):
			a, b, c = 4, 2, 3  # log_2(4) = 2, c > 2
			return work_calc(n, a, b, lambda n: n**c)

	# Case 3: c = log_b a (Balanced case)
	def work_fn_case3(n):
			a, b, c = 4, 2, 2  # log_2(4) = 2, c = 2
			return work_calc(n, a, b, lambda n: n**c)

	# Compare different cases using compare_work
	results1 = compare_work(work_fn_case1, work_fn_case2, sizes)
	print("\nComparing Case 1 (c < log_b a) and Case 2 (c > log_b a):")
	print_results(results1)  # Correct function call

	results2 = compare_work(work_fn_case1, work_fn_case3, sizes)
	print("\nComparing Case 1 (c < log_b a) and Case 3 (c = log_b a):")
	print_results(results2)  # Correct function call

	results3 = compare_work(work_fn_case2, work_fn_case3, sizes)
	print("\nComparing Case 2 (c > log_b a) and Case 3 (c = log_b a):")
	print_results(results3)  # Correct function call
# 	# curry work_calc to create multiple work
# 	# functions taht can be passed to compare_work

# 	# create work_fn1
# 	# create work_fn2
# 	res = compare_work(work_fn1, work_fn2)

# 	print(res)

	
def test_compare_span():
		"""
		Test span calculation by comparing two span functions.
		"""

		# Create span function 1: Based on `span_calc`
		span_fn1 = lambda n: span_calc(n, 2, 2, lambda n: 1)  # Should be O(log n)

		# Create span function 2: A different span calculation
		span_fn2 = lambda n: span_calc(n, 2, 2, lambda n: n)  # Should be O(n)

		# Compare the two span functions
		res = compare_span(span_fn1, span_fn2)

		print(res)