"""PROBLEM
Identify all positions that can be attacked by rooks placed on a mxn chessboard. Rook positions are 0,
and rest of the positions are 1.
"""

"""SOLUTION
In-place solution
Find if the first row and column have rooks. If there are then all the positions in the first row and 
column can be attacked. In the ohter positions if there is a rook present then mark the location in the
first row and column so that all the positions in that row and column can be attacked.
"""

def rook_attack(A):
	m, n = len(A), len(A[0])
	first_row_zero = 0 in A[0]
	first_col_zero = any(not A[i][0] for i in range(m))

	for i in range(1,m):
		for j in range(1,n):
			if A[i][j] == 0:
				A[i][0] = A[0][j] = 0

	for i in range(1,m):
		if not A[i][0]:
			for j in range(1,n):
				A[i][j] = 0

	for j in range(1,n):
		if not A[0][j]:
			for i in range(1,m):
				A[i][j] = 0

	if first_row_zero:
		for j in range(n):
			A[0][j] = 0

	if first_col_zero:
		for i in range(m):
			A[i][0] = 0


A = [[1,0,1,1], [0,1,1,1], [1,1,1,1], [1,0,1,0]]
rook_attack(A)
print(A)
