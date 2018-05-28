# Compute buildings with sunset view

# Approach: Traverse from te end. Use a stack to store the max height buildings (leaders).
# If the subsequent buildings are shorter then add them to the stack.
# Once a taller building is encountered, remove buildings in the stack
# that are shorter than the new building. The, Push the new building to the stack.

def sunset_buildings(A):
	stack = []
	n = len(A)
	stack.append((A[n-1], n-1))

	for i in range(n-2,-1,-1):
		if A[i] < stack[-1][0]:
			stack.append((A[i], i))
		else:
			while A[i] >= stack[-1][0]:
				stack.pop()
				if not stack:
					break
			stack.append((A[i], i))

	# Return building indices
	ids = []
	for b in stack[::-1]:
		ids.append(b[1])

	return ids

buildings = [1,3,1,2,4,2]
res = sunset_buildings(buildings)
print("Buildings heights: {}".format(buildings))
print("Sunset view buildings id: {}".format(res))


