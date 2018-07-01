# The Interval Covering Problem

# Given a set of closed intervals, design an efficient algorithm
# for finding a minimum sized set of numbers that covers all the intervals.

def minimum_visits(intervals):
	if not intervals:
		return []

	# Sort intervals based on right endpoints
	intervals.sort(key=lambda x: x[1])
	visits = []
	last_visit_time = 0

	for interval in intervals:
		if interval[0] > last_visit_time:
			last_visit_time = interval[1]
			visits.append(last_visit_time)

	return visits


intervals = [[1,2], [2,3], [3,4], [2,3], [3,4], [4,5]]
print("Intervals:	{}".format(intervals))

print("Minimum visits set:	{}".format(minimum_visits(intervals)))