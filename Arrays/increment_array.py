""" PROBLEM
	Increment an arbitrary-precision integer

	WAP a program which takes a input an array of digits encoding a nonnegative decimal integer D
	and updates the array to represent the integer D + 1. For example, if the input is [1,2,9] then
	you should update the array to [1,3,0].

"""

""" SOLUTION
	Add 1 to the last element. Reverse the array and if an element is 10 then store 0 at the current
	index and 1 in the previous index. Take care of the case when A[0] = 10 i.e. cases sych as 9, 99, 999

"""

def plus_one(A):
	A[-1] += 1

	for i in reversed(range(1, len(A))):
		if A[i] != 10:
			break
		A[i] = 0
		A[i-1] += 1

	if A[0] == 10:
		# smart way
		A[0] = 1
		A.append(0)

	return A


A = [1,2,9]
print(A)
print("+ 1 = \n{}".format(plus_one(A)))