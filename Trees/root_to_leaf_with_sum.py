""" PROBLEM
	Find a root to leaf path with specified sum

	WAP which takes as input an integer and a binary tree with integer node weights, and checks
	if there exists a leaf whose path weight equals the given integer.

"""

""" SOLUTION
	Keep track of the weight remaining at every recursive call

"""

from TreeNode import Node

def has_path_sum(root, sum_rem):
	if not root:
		return False

	if not root.left and not root.right:
		return root.val == sum_rem

	left = has_path_sum(root.left, sum_rem-root.val)
	right = has_path_sum(root.right, sum_rem-root.val)

	return left or right


s = 7
root = Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(7)

print("Tree has a path with sum = {}:	{}".format(s, has_path_sum(root, s)))