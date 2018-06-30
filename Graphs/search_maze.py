# Search a Maze

import collections

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

def search_maze(maze, s, e):
	# Perform DFS
	def dfs(cur):
		if not(0 <= cur.x < len(maze) and 0 <= cur.y < len(maze[0]) and maze[cur.x][cur.y] == 0):
			return False

		path.append(cur)
		maze[cur.x][cur.y] = 1
		
		if cur == e:
			return True

		if any(map(dfs, (Coordinate(cur.x-1, cur.y), Coordinate(cur.x, cur.y-1), \
		Coordinate(cur.x+1, cur.y), Coordinate(cur.x, cur.y+1)))):
			return True

		# Cannot find path, remove the entry from the path
		del path[-1]
		return False

	path = []
	if not dfs(s):
		return []

	return path

s = Coordinate(0,0)
e = Coordinate(4,4)

maze = [[0,0,0,1,1],
		[0,1,0,0,0],
		[0,1,0,0,1],
		[1,0,1,0,1],
		[0,1,1,0,0]]

print(search_maze(maze, s, e))
