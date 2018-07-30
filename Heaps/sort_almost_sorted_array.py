# WAP to sort a k-sorted array. A k-sorted array is one in which each
# element is at most k away from its correctly sorted position

# T.C.: O(nlogk)

import itertools
import heapq

def sort_approx_sorted_array(sequence,k):
	min_heap = []
	# Adds the first k elements into min_heap
	# Stop if there are fewer than k elements
	for x in itertools.islice(sequence, k):
		heapq.heappush(min_heap,x)

	# For every new element, add it to min_heap and extract the smallest
	for x in sequence:
		smallest = heapq.heappushpop(min_heap,x)
		print(smallest)

	# sequence is exhausted, iteratively extracts the remaining elements
	while min_heap:
		smallest = heapq.heappop(min_heap)
		print(smallest)


sequence = [3,-1,2,6,4,5,8]
k = 2
print("Given sequence: {}\nwith at most: {} positions away".format(sequence,k))
sort_approx_sorted_array(sequence,k)