""" PROBLEM
	Check if a string is palindromic.

"""

""" SOLUTION
	Use 2 pointer technique and check all cases.

"""

def check_palindrome(s):
	i, j = 0, len(s) - 1

	while i < j:
		# skip the alphanumeric characters
		while not s[i].isalnum() and i < j:
			i += 1

		while not s[j].isalnum() and i < j:
			j -= 1

		if s[i].lower() != s[j].lower():
			print(i, j)
			return False

		i += 1
		j -= 1

	return True


s = "able was i, i saw elba"
print("{} - is a palindrome:	{}".format(s, check_palindrome(s))) 