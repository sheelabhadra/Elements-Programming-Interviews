# Given an integer representing a given amount of change
# write a function to compute the minimum number of coins
# required to make that amount of change.

# Recursive solution - Looking at every possible combination
import sys

def makeChange(c):
	if c == 0:
		return 0

	minCoins = sys.maxsize
	for coin in coins:
		if c - coin >= 0:
			curMinCoins = makeChange(c - coin)
			if curMinCoins < minCoins:
				minCoins = curMinCoins

	return minCoins + 1


# Top-Down approach - Recursive
def makeChange_TD(c):
	cache = [-1]*(c+1)
	cache[0] = 0

	return makeChange_TD_helper(c, cache)

def makeChange_TD_helper(c, cache):
	if cache[c] >= 0:
		return cache[c]

	minCoins = sys.maxsize
	for coin in coins:
		if c - coin >= 0:
			curMinCoins = makeChange_TD_helper(c - coin, cache)
			if curMinCoins < minCoins:
				minCoins = curMinCoins

	cache[c] = minCoins + 1
	return cache[c]


# Bottom-Up approach - Iterative
def makeChange_BU(c):
	cache = [-1]*(c+1)
	cache[0] = 0

	for i in range(1,c+1):
		minCoins = sys.maxsize
		for coin in coins:
			if i - coin >= 0:
				curMinCoins = cache[i-coin] + 1
				if curMinCoins < minCoins:
					minCoins = curMinCoins

		cache[i] = minCoins
	
	return cache[c]


coins = [10,6,1]
c = 12
print("Coins:	{}\nChange:	{}".format(coins,c))
print("Minimum number of coins: {}".format(makeChange_BU(12)))




