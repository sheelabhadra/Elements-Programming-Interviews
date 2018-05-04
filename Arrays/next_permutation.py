def next_permutation(perm):
	N = len(perm)
	i = N-2

	# Starting from the right end reach the element
	# in the array till which a decreasing subarray is present.
	# Find k such that p[k] < p[k+1] and entries after after k 
	# appear in decreasing order.
	while i >= 0 and perm[i] > perm[i+1]:
		i -= 1

	if i == -1:
		return []

	k = i
	temp = perm[i]

	# Find the smallest p[l] such that p[l] > p[k].
	while i < N:
		if perm[i] < temp:
			l = i-1
			break
		else:
			i += 1

	# Swap p[l] and p[k]
	perm[k], perm[l] = perm[l], perm[k]

	# Reverse the sequence after position k
	k += 1
	i = k
	j = N-1-i+k
	while i < j:
		perm[i], perm[j] = perm[j], perm[i]
		i += 1
		j -= 1
	return perm


perm = [6, 2, 1, 5, 4, 3, 0]
print('Original array: ', perm)
print('Next permutation: ', next_permutation(perm))









