# Compute the LCA in a BST

## SOLUTION: The first node which is > one node and < than the other node

from TreeNode import Node

def lca(node1, node2, root):
	while root:
		if root.val > node1.val and root.val < node2.val:
			return root

		elif root.val > node1.val and root.val > node2.val:
			root = root.left

		elif root.val < node1.val and root.val < node2.val:
			root = root.right


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

node1 = root.left.left.left
node2 = root.left.right.right

print("The LCA is : {}".format(lca(node1, node2, root).val))