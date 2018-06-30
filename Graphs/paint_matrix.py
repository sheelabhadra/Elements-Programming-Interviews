# Paint a Boolean Matrix
# Flip the color of the selected matrix index
# and all the indices connected to it

# Let WHITE = 0
# BLACK = 1

def flip_color(A, i, j):
	color = A[i][j]

	def dfs(i, j):
		if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] == 1 - color:
			return

		else:
			A[i][j] = 1 - color # Flip color
			dfs(i+1, j)
			dfs(i, j+1)
			dfs(i-1, j)
			dfs(i, j-1)

	dfs(i, j)


A = [[1,0,1,0],
	 [1,0,1,0],
	 [1,0,1,0],
	 [1,0,1,0]]

print("Original matrix: {}".format(A))
x, y = 1, 1
flip_color(A, x, y)

print("After painting ({},{}): {}".format(x,y,A))
