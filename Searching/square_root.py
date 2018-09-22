""" PROBLEM: Compute the integer square root

	WAP which takes a non-negative integer and returns the largest integer whose square is less
	than or equal to the given integer.

"""

""" SOLUTION: Use binary search.

"""

def square_root(num):
	lo, hi = 0, num
	while lo <= hi:
		mid = lo + (hi-lo)//2
		mid_squared = mid*mid

		if mid_squared <= num:
			lo = mid + 1
		else:
			hi = mid - 1
	return lo - 1


num = 50
print("Square root of {} = {}".format(num, square_root(num)))
