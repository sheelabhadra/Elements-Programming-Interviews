# Maximum root to leaf sum path

class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Store all paths in a list
paths = []

def print_path(root, path, s):
	if root == None:
		return

	if root.left == None and root.right == None:
		print("path: ", path + " " + str(root.val), ", sum: ", s + root.val)
		paths.append((path + " " + str(root.val), s + root.val))
		return
	
	else:
		print_path(root.left, path + " " + str(root.val), s + root.val)
		print_path(root.right, path + " " + str(root.val), s + root.val)


root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

print("Root to leaf paths: ")
print_path(root, "", 0)

maxm = paths[0]

for path in paths:
	if maxm[1] < path[1]:
		maxm = path

print("Maximum sum root to leaf path: ", maxm[0])


