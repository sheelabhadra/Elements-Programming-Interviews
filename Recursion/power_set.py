# Generate power set
def power_set(S):
	def helper(to_be_selected, selected_so_far):
		if to_be_selected == len(S):
			power_set.append(list(selected_so_far))
			return

		helper(to_be_selected+1, selected_so_far)

		# Generate all subsets that contain S[to_be_selected]
		helper(to_be_selected+1, selected_so_far + [S[to_be_selected]])

	power_set = []
	helper(0, [])
	return power_set

S = [0,1,2]
res = power_set(S)
print(res)






