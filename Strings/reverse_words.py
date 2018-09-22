""" PROBLEM
	Reverse all the words in a sentence

	Implement a function for reversing the words in a string s.

"""

""" SOLUTION
	Reverse the entire string. Then reverse individual words based on whitespaces.
	Make sure to handle the last word.

"""

def reverse_words(s):
	n = len(s)
	if n == 0:
		return ''.join(s)

	def reverse(s, start, end):
		while start < end:
			s[start], s[end] = s[end], s[start]
			start, end = start+1, end-1

	i, j= 0, 1
	s = s[::-1]
	while j < n:
		if s[j] == ' ':
			reverse(s, i, j-1)
			j += 1
			i = j
		j += 1

	# handle the last word
	reverse(s, i, j-1)
	return ''.join(s)

s = "creativity is intelligence having fun"
print("Original string:\n"+s)
s = list(s)
print("String with reversed words:\n{}".format(reverse_words(s)))