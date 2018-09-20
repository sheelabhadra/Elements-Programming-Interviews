# Push the curent node and its left child
# If root.left is null then pop() and it to the result.
# Add the popped elemnt's right child to the result

from TreeNode import Node

def iterative_inorder(root):
	s, res = [], []
	while s or root:
		if root:
			s.append(root)
			# Going left
			root = root.left
		else:
			# Going up
			root = s.pop()
			res.append(root.val)
			# Going right
			root = root.right

	return res


root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

print("In Order traversal: ", iterative_inorder(root))