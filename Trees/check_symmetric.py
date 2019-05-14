# Test if a binary tree is symmetric

# Write a program that checks whether a binary tree is symmetric

from TreeNode import Node

def is_symmetric(root):
	def check_subtree(root1, root2):
		if not root1 and not root2:
			return True
		if not root1 and root2:
			return False
		if root1 and not root2:
			return False
		return root1.val == root2.val and check_subtree(root1.left, root2.right)\
		 and check_subtree(root1.right, root2.left)

	if not root:
		return True
	return check_subtree(root.left, root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print("Is the tree symmetric?	{}".format(is_symmetric(root)))
