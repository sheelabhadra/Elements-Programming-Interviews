""" The 0-1 Knapsack problem
	An item is in the form of a tuple (weight, value).

"""

""" SOLUTION
	Create 2 cases of selecting and not selecting the current item. The case that gives the higher
	value is selected.

"""


def knapsack_01(items,max_weight):
	dp = [[0]*(max_weight+1) for _ in range(len(items))]

	for i in range(len(dp)):
		for j in range(len(dp[0])):
			if i >= 1:
				without_this_item = dp[i-1][j]
			else:
				without_this_item = 0
			if j >= items[i][0]:
				with_this_item = dp[i][j - items[i][0]] + items[i][1]
			else:
				with_this_item = 0
			dp[i][j] = max(with_this_item, without_this_item)

	return dp[-1][-1]


max_weight = 6
items = [(2,6), (2,10), (3,12)]
print("For the items with (weight, value) = {} and max weight = {}".format(items, max_weight))
print("the max value is: {}".format(knapsack_01(items, max_weight)))