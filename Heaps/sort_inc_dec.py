# WAP for sorting a k-increasing-decreasing array

## SOLUTION: If k << N, we first decompose the array into k sorted arrays
# and then apply merge operation on the sorted arrays
# T.C.: O(nlogk)

from merge_sorted_files import merge_sorted_arrays

def sort_k_inc_dec_array(A):
	sorted_subarrays = []
	INC, DEC = range(2)
	subarray_type = INC
	start_idx = 0

	for i in range(1, len(A)+1):
		if i == len(A) or (A[i-1] < A[i] and subarray_type == DEC) or \
		(A[i-1] >= A[i] and subarray_type == INC):
			sorted_subarrays.append(A[start_idx:i] if subarray_type == INC else A[i-1:start_idx-1:-1])
			start_idx = i
			if subarray_type == INC:
				subarray_type = DEC
			else:
				subarray_type = INC

	return merge_sorted_arrays(sorted_subarrays)


A = [57,131,493,294,221,339,418,452,442,190]
print("Given array:	{}".format(A))
print("Sorted array:	{}".format(sort_k_inc_dec_array(A)))


