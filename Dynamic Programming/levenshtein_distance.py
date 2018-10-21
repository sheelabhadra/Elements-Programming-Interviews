""" Compute the Levenshtein distance
	WAP that takes 2 strings and computes the minimum number of edits needed to transorm
	the first string into the second string.

"""

def levenshtein_dist(s1, s2):
	m, n = len(s2), len(s1)
	dp = [[0]*(n+1) for _ in range(m+1)]

	for i in range(m+1):
		dp[i][0] = i

	for j in range(n+1):
		dp[0][j] = j

	for i in range(1, len(dp)):
		for j in range(1, len(dp[0])):
			if s2[i-1] == s1[j-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				add_last = dp[i-1][j]
				del_last = dp[i][j-1]
				edit = dp[i-1][j-1]
				dp[i][j] = 1 + min(del_s1, del_s2, edit)

	return dp[-1][-1]

s1 = "Carthorse"
s2 = "Orchestra"
print("String 1: {}".format(s1))
print("String 2: {}".format(s2))
print("Levenshtein distance: {}".format(levenshtein_dist(s1,s2)))