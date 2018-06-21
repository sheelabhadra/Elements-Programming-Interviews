# Find the first key greater than a given value in a BST

from TreeNode import Node

def find_first_key(root, k):
	subtree, first_so_far = root, None

	while subtree:
		if subtree.val > k:
			subtree, first_so_far = subtree.left, subtree
		
		# Skip the left subtree as root and all keys are <= k
		else:
			subtree = subtree.right

	return first_so_far


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

print("The first key > 23 is: {}".format(find_first_key(root, 23).val))