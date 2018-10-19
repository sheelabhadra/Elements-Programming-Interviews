""" PROBLEM
	WAP that takes a final score and scores for individual plays, and returns the number
	of combinations of plays that result in the final score.

"""

""" SOLUTION
	2 cases: when the current individual play score is included and the other when it is excluded

"""

def num_combinations(final_score, individual_play_scores):
	dp = [[0]*(final_score + 1) for x in range(len(individual_play_scores))]
	# one way to reach 0
	for i in range(len(dp)):
		dp[i][0] = 1

	for i in range(len(dp)):
		for j in range(1, len(dp[0])):
			if i >= 1:
				without_this_play = dp[i-1][j]
			else:
				without_this_play = 0
			if j >= individual_play_scores[i]:
				with_this_play = dp[i][j - individual_play_scores[i]]
			else:
				with_this_play = 0
			dp[i][j] = with_this_play + without_this_play
	return dp[-1][-1]


final_score = 12
individual_play_scores = [2,3,7]
print(num_combinations(final_score, individual_play_scores))


