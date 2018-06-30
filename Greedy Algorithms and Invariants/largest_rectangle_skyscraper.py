# Compute the largest rectangel under the skyline

def largest_rectangle(heights):
	temp = [] # to hold the max rectangles
	stack = [] # to keep track of the smallest height so far

	heights.append(0)

	for i,h in enumerate(heights):
		cur_pos = i
		while stack and h < stack[-1][0]:
			cur_h, cur_pos = stack.pop()
			temp.append(cur_h*(i - cur_pos))
		stack.append([h, cur_pos])

	if temp:
		return max(temp)
	else:
		return 0


heights = [1,4,2,5,6,3,2,6,6,5,2,1,3]
print("Heights:	{}".format(heights))

print("Largest rectangle area:	{}".format(largest_rectangle(heights)))