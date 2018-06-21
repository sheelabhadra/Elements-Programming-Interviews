# Find the k Largest elements in a BST

# Brute-force approach: In-order traversal and pick the last k elements

# Better solution: Begin with the desired nodes and work backwards. Reverse in-order visit.
# First recurse on the right subtree and then on the left subtree.

from TreeNode import Node

def k_largest_elements(root, k):
	# Perform reverse in-order traversal
	def helper(root):
		if root and len(k_largest) < k:
			helper(root.right)
			if len(k_largest) < k:
				k_largest.append(root.val)
				helper(root.left)

	k_largest = []
	helper(root)
	return k_largest


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

k = 4
print("The k = {} largest elements are: {}".format(k, k_largest_elements(root, k)))