# Compute an Optimum Assignment of Tasks

# Given the duration of tasks where each task is independent of each other
# Each worker can be assigned exactly 2 tasks
# Minimize the maximum time that would be taken to finish the tasks

## SOLUTION: Sort the times; combine the 1st and the last, 2nd and the 2nd last and so on

def optimum_task_assignment(times):
	times.sort()
	durations = []

	i, j = 0, len(times)-1
	while i < j:
		durations.append(times[i] + times[j])
		i += 1
		j -= 1
	return max(durations)


times = [5,2,1,6,4,4]
print("The duration of the tasks:	{}".format(times))

print("Minimum time taken to finish tasks:	{}".format(optimum_task_assignment(times)))
