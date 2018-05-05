# Push the curent node and its left child
# If root.left is null then pop() and it to the result.
# Add the popped elemnt's right child to the result

class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def iterative_inorder(root):
	s, r, res = [], [], []
	while s or root:
		if root:
			s.append(root)
			root = root.left
		else:
			root = s.pop()
			r.append(root)
			root = root.right

	res = []
	while r:
		res.append(r.pop(0).val)

	return res


root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

print("In Order traversal: ", iterative_inorder(root))