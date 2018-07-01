# Find the majority element

# Given a stream of charactres, determine the majority element. It is
# known that one of the characters occurs more than half the times.

def find_majority_element(input_stream):
	candidate, candidate_count = None, 0

	for e in input_stream:
		if candidate_count == 0:
			candidate, candidate_count = e, candidate_count + 1
		elif candidate == e:
			candidate_count += 1
		else:
			candidate_count -= 1
	return candidate

input_stream = ['b','a','c','a','a','b','a','a','c','a']
print("Stream:	{}".format(input_stream))

print("Majority element:	{}".format(find_majority_element(input_stream)))