# Rotate an array by 'i' positons to the right in-place

def rotate_array(A, i):
	# Reverse the array
	A = A[::-1]
	# Reverse the array till i
	A[:i] = A[:i][::-1]
	# Reverse the array after i
	A[i:] = A[i:][::-1]

	return A

A = [1,2,3,4,5,6]
print("Given array: {}".format(A))
print("Array rotated by {} places: {}".format(3,rotate_array(A, 3)))  