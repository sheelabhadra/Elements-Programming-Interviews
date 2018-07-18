# Given an integer array in which each entry but one apperas in triplicate
# with the remaining element appearing once, find the element appearing once.

# e.g. if the array is [2,4,2,5,2,5,5], return 4

## SOLUTION: The key step here is to count % 3 for each bit position
# This eliminates the elements that appear 3 times.
# So, the bit-positions which have a count of 1 are exactly
# the bit-positions in the count that are set to 1.

def find_element_appears_once(A):
	counts = [0]*32

	for x in A:
		for i in range(32):
			counts[i] += x & 1
			x >>= 1

	def handle_negative(n):
		if n < 2**31:
			return n
		else:
			return n - 2**32

	return handle_negative(sum(1<<i for i,c in enumerate(counts) if c%3))

A = [2,4,2,5,2,5,5]
print("Array:	{}".format(A))

print("Element appearing once:	{}".format(find_element_appears_once(A)))