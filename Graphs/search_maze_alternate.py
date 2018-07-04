# Check if there's path from source to destination in a maze

def grid_path(grid,s,e):
		dfs(grid,s[0],s[1],e)
		if grid[e[0]][e[1]] == "#":
			return True

		else:
			return False

def dfs(grid,i,j,e):
	if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 0:
		return

	else:
		grid[i][j] = "#"
		dfs(grid,i+1,j,e)
		dfs(grid,i,j+1,e)
		dfs(grid,i-1,j,e)
		dfs(grid,i,j-1,e)


grid = [[0,0,0,1,1],
		[0,1,0,0,0],
		[0,1,0,0,1],
		[1,0,1,0,1],
		[0,1,1,0,0]]

print(grid_path(grid,(2,0),(4,4)))
print(grid)