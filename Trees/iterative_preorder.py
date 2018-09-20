""" SOLUTION
	Use a stack. It is initailized containing the root. Visit it by popping it. First add
	its right child and then its left child to the stack.

"""

from TreeNode import Node

def iterative_preorder(root):
	s = [root]
	res = []

	while s:
		root = s.pop()
		res.append(root.val)
		if root.right:
			s.append(root.right)
		if root.left:
			s.append(root.left)
	return res


root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

print("Pre Order traversal: ", iterative_preorder(root))