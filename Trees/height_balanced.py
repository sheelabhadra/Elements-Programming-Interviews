# Test if a binary tree is height balanced

# Write a program that takes in input the root of a binary tree and checks whether 
# the tree is height balanced.

## SOLUTION: At each node store a tuple containing info if the tree is balanced 
# and the height of the tree upto the node.

from TreeNode import Node

def is_balanced_binary_tree(root):
	def check_balanced(root):
		if not root:
			return (True, -1) # Base case
		left_res = check_balanced(root.left)
		if not left_res[0]:
			# Left subtree is not balanced
			return (False, 0)
		right_res = check_balanced(root.right)
		if not right_res[0]:
			# Right subtree is not balanced
			return (False, 0)

		if abs(left_res[1] - right_res[1]) <= 1:
			is_balanced = True
		else:
			is_balanced = False
		# Find height of the subtree
		height = max(left_res[1], right_res[1]) + 1
		return (is_balanced, height)

	return check_balanced(root)[0]


root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

print("Is the tree height balanced?	{}".format(is_balanced_binary_tree(root)))