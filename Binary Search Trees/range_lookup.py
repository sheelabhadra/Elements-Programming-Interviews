# The range lookup problem
# returns the nearest point to a particular point

# Write a program that takes as input a BST and an interval and returns 
# the BST keys that lie in the interval

## SOLUTION:
# 1. If the root of the tree holds a key < left endpoint of the interval, left subtree
#    cannot contain any node whose key lies in the interval
# 2. If the root of the tree holds a key > right endpoint of the interval, right subtree
#    cannot contain any node whose key lies in the interval
# 3. Else, the root of the tree holds a key that lies within the interval, and it is possible
#    for both the left and right subtrees to contain nodes whose keys lie in teh interval

# Apply the logic recursively to all nodes in the BST

from TreeNode import Node

def range_lookup_bst(root, interval):
	def helper(root):
		if not root:
			return None

		if interval[0] <= root.val <= interval[1]:
			# root.val lies in the interval
			helper(root.left)
			result.append(root.val)
			helper(root.right)

		elif interval[0] > root.val:
			helper(root.right)

		else:
			helper(root.left)

	result = []
	helper(root)
	return result

root = Node(19)
root.left = Node(7)
root.right = Node(43)
root.left.left = Node(3)
root.left.right = Node(11)
root.left.left.left = Node(2)
root.left.left.right = Node(5)
root.left.right.right = Node(17)
root.left.right.right.left = Node(13)

root.right.left = Node(23)
root.right.right = Node(47)
root.right.left.right = Node(37)
root.right.right.right = Node(53)
root.right.left.right.left = Node(29)
root.right.left.right.right = Node(41)
root.right.left.right.left.right = Node(31)

interval = [16, 31]

print("The nodes within the interval: {}".format(range_lookup_bst(root, interval)))