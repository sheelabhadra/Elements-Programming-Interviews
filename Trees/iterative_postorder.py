from TreeNode import Node

def iterative_postorder(root):
	# Using 2 stacks: 1 for DFs, another for storing the pop() sequence
	if root == None:
		return []

	s1, s2 = [root], []

	while s1:
		root = s1.pop()
		s2.append(root)
		if root.left:
			s1.append(root.left)
		if root.right:
			s1.append(root.right)
	
	res = []

	while s2:
		res.append(s2.pop().val)

	return res

root = Node(1)
root.left = Node(-10)
root.right = Node(11)
root.left.right = Node(5)
root.left.right.right = Node(3)
root.right.left = Node(13)
root.right.right = Node(16)

print("Post order traversal: ", iterative_postorder(root))