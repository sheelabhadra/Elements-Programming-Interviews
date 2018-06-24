# Find the closest entries in 3 sorted arrays

## SOLUTION: Pick the first 3 elements from the 3 arrays and compare the minm and the maxm.
# Remove the minm element and insert the next elemet from the corresponding array.
# For 'k' sorted arrays, BST is used as we need to repeatedly insert, delete, 
# find the minm, and find the maxm amongst a collecton of 'k' elements.

import bintrees

def find_closest_entries(sorted_arrays):
	min_so_far = float('inf')

	# Stores array iterators in each entry
	iters = bintrees.RBTree()

	for idx, sorted_array in enumerate(sorted_arrays):
		it = iter(sorted_array)
		first_min = next(it, None)
		if first_min:
			iters.insert((first_min, idx), it)

	while True:
		min_value, min_idx = iters.min_key()
		max_value = iters.max_key()[0]
		min_so_far = min(max_value - min_value, min_so_far)
		it = iters.pop_min()[1]
		next_min = next(it, None)

		# Return if some array has no remaining elements
		if not next_min:
			return min_so_far, min_value, max_value

		iters.insert((next_min, min_idx), it)

A1 = [5,10,15]
A2 = [3,6,9,12,15]
A3 = [8,16,24]

print(find_closest_entries([A1,A2,A3]))