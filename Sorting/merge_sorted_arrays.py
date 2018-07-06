# Merge 2 sorted arrays

def merge_two_sorted_arrays(A, m, B, n):
	i, j, idx = m-1, n-1, m+n-1
	
	while i >=0 and j >= 0:
		if A[i] > B[j]:
			A[idx] = A[i]
			i -= 1
		else:
			A[idx] = B[j]
			j -= 1
		idx -= 1

	# If there are still elements left in B
	while j >= 0:
		A[idx] = B[j]
		j -= 1
		idx -= 1

	return A

A = [5,13,17]
B = [3,7,11,19]
print("A:	{}".format(A))
print("B:	{}".format(B))

m = len(A)
n = len(B)

A.extend([0]*n)

print("Merged arrays:	{}".format(merge_two_sorted_arrays(A, m, B, n)))