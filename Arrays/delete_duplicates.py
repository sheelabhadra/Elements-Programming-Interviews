""" PROBLEM
	Delete duplicates from a sorted array.

	WAP which takes as input a sorted array and updates it so that all duplicates have been
	removed and the remaining elemnts have been shifted to left to fill the emptied indices.
	Return the number of valid elements.

"""

""" SOLUTION
	Since the array is sorted the repeated elements will appear together. So keep shifting the
	iterator 'i' when repetition occurs. When there is no repetition increment 'write_index' and
	replace the element at 'write_index' with the elemnt at 'i'.

"""

def delete_duplicates(A):
	if not A:
		return 0

	write_index = 1
	for i in range(1, len(A)):
		if A[write_index - 1] != A[i]:
			A[write_index] = A[i]
			write_index += 1

	return write_index


A = [2,3,5,5,7,11,11,11,13]
delete_duplicates("Valid entries in {}: {}".format(A, delete_duplicates(A)))
