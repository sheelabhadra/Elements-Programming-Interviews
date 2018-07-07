# Compute the nth Fibonacci number

# Recursive solution
def fib_rec(n):
	if n < 2:
		return n
	return fib_rec(n-1) + fib_rec(n-2)


# Top-down approach - Recursive
def fib_TD(n):
	if n < 2:
		return n

	cache = [-1]*(n+1)
	cache[0], cache[1] = 0, 1

	return fib_TD_helper(n, cache)

def fib_TD_helper(n, cache):
	if cache[n] >= 0:
		return cache[n]

	cache[n] = fib_TD_helper(n-1, cache) + fib_TD_helper(n-2, cache)
	return cache[n]


# Bottom-up approach - Iterative
def fib_BU(n):
	if n < 2:
		return n

	cache = [-1]*(n+1)
	cache[0], cache[1] = 0, 1

	for i in range(2, n+1):
		cache[i] = cache[i-1] + cache[i-2]

	return cache[n]

n = int(input("Enter the value of N:	"))
print("{}th Fibonacci number:	{}".format(n, fib_BU(n)))
