import random

def online_random_sample(it, k):
	sampling_results = it[:k]

	num_seen_so_far = k

	for x in it:
		idx_to_replace = random.randrange(num_seen_so_far)

		# Generate a random number in [0, num_seen_so_far - 1], and if this
		# number is in [0, k-1], we replace that element from the sample
		# with x
		if idx_to_replace < k:
			sampling_results[idx_to_replace] = x

	return sampling_results

it = ['p','q','r','t','u','v']

print('Data Stream: ', it)
print('Random subset: ', online_random_sample(it, 2))
