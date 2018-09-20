""" PROBLEM
	Sum the root-to-leaf paths in a binary tree

	Design an algorithm to computer the sum of the binary numbers represented by
	the root-to-leaf paths.

"""

""" SOLUTION
	To compute the integer for the path from the root to any node, take the integer value
	of the node's parent, double it and add the bit at that node.

"""

from TreeNode import Node

def sum_root_to_leaf(root, partial_path_sum=0):
	if not root:
		return 0

	partial_path_sum = partial_path_sum*2 + root.val
	if not root.left and not root.right:
		return partial_path_sum

	left_sum = sum_root_to_leaf(root.left, partial_path_sum)
	right_sum = sum_root_to_leaf(root.right, partial_path_sum)

	return left_sum + right_sum


root = Node(1)
root.left = Node(0)
root.right = Node(1)
root.left.left = Node(0)
root.left.right = Node(1)
root.right.left = Node(0)
root.right.right = Node(0)

print("The sum of root to leaf = {}".format(sum_root_to_leaf(root)))