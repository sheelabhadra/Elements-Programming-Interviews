def merge_sort(arr, left, right):
	if left >= right:
		return []
	if left == right - 1:
		return [arr[left]]
	
	mid = left + (right - left) / 2
	left_sorted_half = merge_sort(arr, left, mid)
	right_sorted_half = merge_sort(arr, mid, right)
	
	l = 0
	r = 0
	ans = []
	while l < len(left_sorted_half) and r < len(right_sorted_half):
		if left_sorted_half[l] < right_sorted_half[r]:
			ans.append(left_sorted_half[l])
			l += 1
		else:
			ans.append(right_sorted_half[r])
			r += 1
	
	if l < len(left_sorted_half):
		ans.extend(left_sorted_half[l:])
	else:
		ans.extend(right_sorted_half[r:])
	return ans

a = [7,6,4,3,5,8,2,1]
print("Orig array:	{}".format(a))
print("Sorted array:	{}".format(merge_sort(a, 0, len(a))))
