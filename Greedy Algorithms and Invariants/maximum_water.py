# Factset ML Engineer Interview Question

# Compute the maximum water trapped by a pair of vertical lines

## SOLUTION: Use 2 pointer method

def max_water_trapped(heights):
	i, j = 0, len(heights)-1
	max_water = 0

	while i < j:
		width = j - i
		max_water = max(max_water, width*min(heights[i], heights[j]))

		if heights[i] < heights[j]:
			i += 1
		else:
			j -= 1

	return max_water

heights = [1,2,1,3,4,4,5,6,2,1,3,1,3,2,1,2,4,1]

print("Heights:	{}".format(heights))

print("Max water trapped:	{}".format(max_water_trapped(heights)))


