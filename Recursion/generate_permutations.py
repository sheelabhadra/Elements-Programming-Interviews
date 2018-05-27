# Generate all permutations of an array with distinct elements
def gen_perm(arr):
	def perm_helper(i):
		if i == len(A) - 1:
			res.append(arr.copy())
			return

		for j in range(i, len(arr)):
			arr[j], arr[i] = arr[i], arr[j] # swap
			perm_helper(i+1) # generate all permutations for arr[i+1:]
			arr[j], arr[i] = arr[i], arr[j] # swap

	res = []
	perm_helper(0)
	return res

A = [1,2,3]
res = gen_perm(A)
print(res)
