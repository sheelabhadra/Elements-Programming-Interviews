from TreeNode import Node

def lca_BT(root, node1, node2):
	if root == None:
		return None

	if root == node1 or root == node2:
		return root

	left = lca_BT(root.left, node1, node2)
	right = lca_BT(root.right, node1, node2)

	if left and right:
		return root

	elif not left and not right:
		return None

	elif not left and right:
		return right

	else:
		return left

root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

node1 = root.left.right
node2 = root.right.left

print("LCA of {} and {} is : {}".format(node1.val, node2.val, lca_BT(root, node1, node2).val))