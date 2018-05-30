# Find the first missing postive entry

def missing_positive(A):
	n = len(A)

	# Swap so that A[i-1] = i
	for i in range(n):
		while 1 <= A[i] <= n and A[i] != A[A[i]-1]:
			A[A[i]-1], A[i] = A[i], A[A[i]-1]

	# 2nd pass: Find the first position where the violation occurs
	for i in range(n):
		if i != A[i]-1:
			return i+1

A = [3,5,4,-1,5,1,-1]
print("Given array: {}".format(A))
res = missing_positive(A)
print("1st missing positive number: {}".format(res))
