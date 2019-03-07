# Let A be an array of integers. Call the pair of indices (i,j) inverted if i < j and A[i] > A[j]. 
# e.g. if A = [4,1,2,3], then the pair of indices (0,3) is inverted.

# Design an efficient algorithm that takes an array of integers and returns the number of
# inverted pairs of indices.

def count_inversions(A):
	# Get number of inversions in A[start:end]
	def count_subarray_inversions(start, end):
		# Merge 2 sorted subarrays A[start:mid], A[mid:end]
		def merge_and_count_inversions(start, mid, end):
			sorted_A = []
			left_start, right_start, inversion_count = start, end, 0

			while left_start < mid and right_start < end:
				if A[left_start] <= A[right_start]:
					sorted_A.append(A[left_start])
					left_start += 1
				else:
					inversion_count += mid - left_start
					sorted_A.append(A[right_start])
					right_start += 1

			A[start:end] = sorted_A + A[left_start:mid] + A[right_start:end]

			return inversion_count

		if end - start <= 1:
			return 0

		mid = start + ((end - start)//2)

		return (count_subarray_inversions(start, mid) + count_subarray_inversions(mid, end) + \
			merge_and_count_inversions(start, mid, end))

	return count_subarray_inversions(0, len(A))


A = [3,6,4,2,5,1]
print("Array:	{}".format(A))
print("Number of inversions:	{}".format(count_inversions(A)))