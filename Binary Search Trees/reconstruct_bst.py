# Reconstruct a BST from traversal data

## SOLUTION: Preorder traversal gives unique BST representation.
# First node = root
# Second node = left subtree
# Final subsequence with keys > first node = right subtree

from TreeNode import Node

def inorder_traversal(root):
	if not root:
		return None

	if root.left:
		inorder_traversal(root.left)

	inorder.append(root.val)

	if root.right:
		inorder_traversal(root.right)


def reconstruct_bst(preorder):
	if not preorder:
		return None

	transition_point = next((i for i,a in enumerate(preorder) if a > preorder[0]), len(preorder))

	# for idx in range(1, len(preorder)):
	# 	if preorder[idx] > preorder[0]:
	# 		transition_point = idx
	# 		break

	root = Node(preorder[0])
	root.left = reconstruct_bst(preorder[1:transition_point])
	root.right = reconstruct_bst(preorder[transition_point:])

	return root

preorder = [43, 23, 37, 29, 31, 41, 47, 53]

tree = reconstruct_bst(preorder)

inorder = []

inorder_traversal(tree)

print("Inorder traversal of the tree: {}".format(inorder))
