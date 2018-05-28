# Generate all subsets of size k
def subset_k(n,k):
	def helper(offset, partial_subset):
		if len(partial_subset) == k:
			res.append(list(partial_subset))
			return

		num_remaining = k - len(partial_subset)
		
		i = offset
		while i <= n and num_remaining <= n - i + 1:
			helper(i+1, partial_subset + [i])
			i += 1

	res = []
	helper(1, [])
	return res

n = 6
ss = subset_k(n,2)
print(ss)


