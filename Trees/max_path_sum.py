# Maximum Path Sum in a Binary Tree
# Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.


# For every node, check 4 cases:
# 1. Node omly
# 2. Node + left child
# 3. Node + right child
# 4. Node + left child + right child

from TreeNode import Node

def findMaxUtil(root):
	if not root:
		return 0

	l = findMaxUtil(root.left)
	r = findMaxUtil(root.right)

	# Max path for parent call of root. This path 
    # must include at most one child of root
	max_single = max(max(l, r) + root.val, root.val)

	# Max top represents the sum when the node under
    # consideration is the root of the maxSum path and
    # no ancestor of root are there in max sum path
	max_top = max(max_single, l+r+ root.val)

	findMaxUtil.res = max(findMaxUtil.res, max_top)

	return max_single

def findMaxSum(root):
	# Static variable to store the changes
	findMaxUtil.res = float('-inf')
	
	findMaxUtil(root)

	return findMaxUtil.res


root = Node(10)
root.left = Node(2)
root.right   = Node(10)
root.left.left  = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left   = Node(3)
root.right.right.right  = Node(4)

print("Max path sum is " ,findMaxSum(root))

