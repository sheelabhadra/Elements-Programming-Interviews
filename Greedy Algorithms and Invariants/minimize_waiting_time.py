# Schedule to minimize waiting time

# Given service times for a set of queries, compute a schedule for processing the 
# queries that minimizes the total waiting time

## SOLUTION: Sort the service time array. As lower service time in the beginning
# will reduce the total waiting time.

def minimum_total_waiting_time(service_times):
	service_times.sort()

	total_waiting_time, cur_time = 0, 0

	for i in range(len(service_times)-1):
		cur_time += service_times[i]
		total_waiting_time += cur_time

	return total_waiting_time

service_times = [2,5,3,1]
print("Service times:	{}".format(service_times))

print("Minimum total waiting time:	{}".format(minimum_total_waiting_time(service_times)))
