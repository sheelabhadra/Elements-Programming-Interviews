# WAP that takes as inout a set of sorted sequences and computes the 
# union of these sequences as a sorted sequence.
# e.g.: Input: [3,5,7], [0,6], [0,6,28]
#	    Output: [0,0,3,5,6,6,7,28]

## SOLUTION: Keep a min-heap as it is ideal for maintaining a collection
# of elements when we need to add arbitrary values and extract the 
# smallest element

import heapq

def merge_sorted_arrays(sorted_arrays):
	min_heap = []

	# Builds a list of iterators for each array in sorted_arrays - Powerful!
	# This is helpful because we won't need to keep track of the indices of 
	# the individual arrays separately
	sorted_arrays_iters = [iter(x) for x in sorted_arrays] 

	# Put first element from each array into min-heap
	for i, it in enumerate(sorted_arrays_iters):
		first_element = next(it, None)
		if first_element is not None:
			heapq.heappush(min_heap, (first_element, i))

	result = []
	while min_heap:
		smallest_entry, smallest_array_i = heapq.heappop(min_heap)
		smallest_array_iter = sorted_arrays_iters[smallest_array_i]
		result.append(smallest_entry)

		next_element = next(smallest_array_iter, None)
		if next_element is not None:
			heapq.heappush(min_heap, (next_element, smallest_array_i))

	return result


sorted_arrays = [[3,5,7], [0,6], [0,6,28]]
print("Sorted arrays:\n{}".format(sorted_arrays))
print("Merged arrays: {}".format(merge_sorted_arrays(sorted_arrays)))