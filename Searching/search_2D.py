""" PROBLEM
	Search in a 2D sorted array

	WAP to if a number exists in a 2D sorted array.

"""

""" SOLUTION
	Start from the top right corner. This eleminates a row and a column together 
	in every comparison.
	T.C.: O(m+n)

"""

def matrix_search(A, num):
	row, col = 0, len(A[0]) - 1

	while row < len(A) and col >= 0:
		if A[row][col] == num:
			return True
		elif A[row][col] < num:
			# eliminate the row
			row += 1
		else:
			# eliminate the column
			col -= 1

	return False


A = [[-1,2,4,4,6], [1,5,5,9,21], [3,6,6,9,22], [3,6,8,10,24], [6,8,9,12,25], [8,10,12,13,40]]
num = 8
print("Matrix: {}".format(A))
print("{} is present in the matrix: {}".format(num, matrix_search(A, num)))
