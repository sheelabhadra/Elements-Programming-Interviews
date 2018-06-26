# Build a minimum height BST from a sorted array

from TreeNode import Node

def build_min_height_bst(A):
	def helper(start, end):
		if start >= end:
			return None
		mid = start + (end - start)//2

		root = Node(A[mid])
		root.left = helper(start, mid)
		root.right = helper(mid+1, end)

		return root

	return helper(0, len(A))


def height(root):
	if not root:
		return 0

	else:
		lh = height(root.left)
		rh = height(root.right)

		return max(lh,rh) + 1


A = [2,3,4,5,7,11,13,17,19,23]

tree = build_min_height_bst(A)

h = height(tree)

print("Minimum height the tree: {}".format(h))