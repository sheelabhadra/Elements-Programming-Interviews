"""PROBLEM:
Design an efficient algorithm for computing the skyline.
"""

"""SOLUTION:
Find the left-most and the right-most coordinate among all the buildings. Within this range
for each building we iterate over the coordinates, and update the skyline.
T.C.: O(nW), W - width of the widest building 
"""
import collections

Rectangle = collections.namedtuple('Rectangle', ('left', 'right', 'height'))

def skyline(buildings):
	min_left = min(buildings, key=lambda b: b.left).left
	max_right = max(buildings, key=lambda b: b.right).right

	heights = [0]*(max_right - min_left + 1)

	for building in buildings:
		for i in range(building.left, building.right + 1):
			heights[i - min_left] = max(heights[i - min_left], building.height)

	return heights


buildings = [Rectangle(5,9,2), Rectangle(1,6,3), Rectangle(4,8,4), Rectangle(0,3,1), Rectangle(7,10,3)]
print("Buildings: {}".format(buildings))
print("Skyline: {}".format(skyline(buildings)))
