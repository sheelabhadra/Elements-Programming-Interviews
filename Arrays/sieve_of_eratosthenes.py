""" PROBLEM
	Enumerate all primes to n

	WAP a program that takes an integer argument and returns all the primes between 1 and that integer.

"""

""" SOLUTION
	Sieve of Eratosthenes: Create an array 'isPrime' of size n+1 in which set set all the prime numbers to 1 and 
	the non-prime numbers to 0. Initially, set isPrime[0] = 0 and isPrime[1] = 0 for the numbers 0 and 1. Set 
	the rest of the array elements as 1. For index >= 2, if isPrime[index] == 1 then append it to the liast of 
	prime numbers and then set all multiples of 'index' to 0 in iSprime array since the multiples will be 
	non-prime.

"""

def generate_primes(n):
	primes = []

	# Boolean array to keep track of the numbers eliminated
	isPrime = [0, 0] + [1]*(n - 1)

	for p in range(2, n+1):
		if isPrime[p]:
			primes.append(p)

			# Sieve p's multiples
			for i in range(p, n+1, p):
				isPrime[i] = 0

	return primes


n = 100
print("The prime numbers till {} are\n{}".format(n, generate_primes(n)))