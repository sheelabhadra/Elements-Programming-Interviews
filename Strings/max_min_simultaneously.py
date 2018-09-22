""" PROBLEM
	Find the min and max simultaneously

"""

""" SOLUTION
	Compare every pair with a step size of 2. Compute the local min and local max 
	for each pair and update the global min and global max.

"""

def find_min_max(A):
	def min_max(a,b):
		if a < b:
			return a, b
		else:
			return b, a

	if len(A) == 1:
		return (A[0], A[0])

	global_minm, global_maxm = min_max(A[0], A[1])

	for i in range(2, len(A)-1, 2):
		local_minm, local_maxm = min_max(A[i], A[i+1])
		global_minm, global_maxm = min(local_minm, global_minm), max(local_maxm, global_maxm)
	
	# odd elements case
	if len(A)%2 == 1:
		global_minm, global_maxm = min(A[-1], global_minm), max(A[-1], global_maxm)

	return global_minm, global_maxm 


A = [3,2,5,1,2,4]
res = find_min_max(A)
print("Array: {}\nMin: {}, Max: {}".format(A, res[0], res[1]))

