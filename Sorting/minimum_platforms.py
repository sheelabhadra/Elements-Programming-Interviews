# Minimum number of platforms required for a Railway/Bus Station
# Alternate question: Minimum number of meeting rooms

def min_platforms(arr, dep):
	arr.sort()
	dep.sort()

	count, max_so_far = 1, 0
	a, d = 1, 0

	while a < len(arr) and d < len(dep):
		if arr[a] <= dep[d]:
			count += 1
			max_so_far = max(count, max_so_far)
			a += 1
		else:
			count -= 1
			d += 1

	return max_so_far


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1120, 1130, 1200, 1900, 2000]
print("Arrival times:	{}\nDeparture times:	{}".format(arr, dep))

print("Minimum platforms:	{}".format(min_platforms(arr, dep)))



