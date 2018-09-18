""" PROBLEM
	The Dutch National Flag Problem

"""

""" SOLUTION
	Create 3 groups lo, mid, and hi. Swap elements depending on which group they should
	go to.

"""

def dutch_flag_problem(A):
	lo, mid, hi = 0, 0, len(A)-1

	while mid <= hi:
		if A[mid] < A[lo]:
			A[lo], A[mid] = A[mid], A[lo]
			lo += 1
			mid += 1
		elif A[mid] == A[lo]:
			mid += 1
		else:
			A[hi], A[mid] = A[mid], A[hi]
			hi -= 1

	return A


A = [1,2,0,0,1,2,1,0]
print("Original array:	{}".format(A))
print("After sorting:	{}".format(dutch_flag_problem(A)))