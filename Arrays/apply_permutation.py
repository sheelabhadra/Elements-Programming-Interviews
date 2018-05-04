def apply_permutation(perm, A):
	for i in range(len(A)):
		next = i;
		while perm[next] >= 0:
			A[i], A[perm[next]] = A[perm[next]], A[i]
			temp = perm[next]
			perm[next] -= len(perm)
			next = temp
	
	perm[:] = [a+len(perm) for a in perm]

A = [1,2,3,4]
perm = [3,1,2,0]
apply_permutation(A,perm)
