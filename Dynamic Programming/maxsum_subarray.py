def max_sum_subarray(A):
	min_sum, max_sum = 0, 0

	# running sum to keep track of sum till 'i'
	sum_i = []
	temp = 0
	for e in A:
		temp += e 
		sum_i.append(temp)

	start, end = 0, 0
	for running_sum in sum_i:
		if min_sum <= running_sum:
			min_sum = min_sum
		else:
			min_sum = running_sum
			start += 1
		# min_sum = min(min_sum, running_sum)
		if max_sum >= running_sum - min_sum:
			max_sum = max_sum
		else:
			max_sum = running_sum - min_sum
			end += 1
		# max_sum = max(max_sum, running_sum - min_sum)

	return max_sum, start, end


A = [904,40,523,12,-335,-385,-124,481,-31]
print("Original array:	{}".format(A))
print("Max sum subarray:	Sum {}, Start idx {}, End idx {}".format(max_sum_subarray(A)[0], max_sum_subarray(A)[1], max_sum_subarray(A)[2]))