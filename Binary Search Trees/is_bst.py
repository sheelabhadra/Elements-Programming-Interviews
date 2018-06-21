# Test if a binary tree supports BST property

from TreeNode import Node

def is_bst(root, low=float('-inf'), high=float('inf')):
	if not root:
		return True

	if high <= root.val <= low:
		return False

	return is_bst(root.left, low, root.val) and is_bst(root.right, root.val, high)


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

print("The given tree is a BST: {}".format(is_bst(root)))