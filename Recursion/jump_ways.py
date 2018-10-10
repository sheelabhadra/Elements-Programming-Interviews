""" PROBLEM
	Find the number of ways a frog can climb a stair case if it can either take 1 step
	or 2 steps at a time.
"""

""" SOLUTION
	If the frog jumps 1(2) step(s) then next it can cover the remaining steps in 1 or 2 jumps.
"""

def jump_ways(n):
	if n == 1:
		return 1
	if n == 0:
		return 1
	return jump_ways(n-1) + jump_ways(n-2)


n = 11
print("Number of ways for {} steps: {}".format(n, jump_ways(n)))