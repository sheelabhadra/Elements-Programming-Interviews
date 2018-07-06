# Compute the intersection of 2 sorted arrays

def intersect_two_sorted_arrays(A, B):
	i, j = 0, 0

	intersection = []

	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			i += 1
		elif A[i] < B[j]:
			j += 1
		else:
			# Check for repeated elements
			# Check the 0th element
			if i == 0 or A[i] != A[i-1]:
				intersection.append(A[i])
			i += 1
			j += 1

	return intersection

A = [2,3,3,5,5,6,7,7,8,12]
B = [5,5,6,8,8,9,10,10]

print(intersect_two_sorted_arrays(A,B))
