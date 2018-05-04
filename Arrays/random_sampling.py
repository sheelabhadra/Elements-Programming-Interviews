import random

def random_sampling(k, A):
	for i in range(k):
		# Generate a random index in [i, len(A)-1]
		r = random.randint(i, len(A)-1)
		A[i], A[r] = A[r], A[i]
	return A[:k]

A = [3,7,5,11]
print('Given array: ', A)
print('Random subset: ', random_sampling(3, A))
