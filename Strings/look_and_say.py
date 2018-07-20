def look_and_say(n):
	s = ['1']

	for _ in range(n-1):
		new_s = []
		i, j = 0, 0
		count = 1

		while j < len(s):
			if s[i] == s[j]:
				j += 1
			else:
				count = j-i
				new_s.append(str(count))
				new_s.append(str(s[i]))
				count = 1
				i = j
				j += 1

		if j == len(s):
			count = j-i
			new_s.append(str(count))
			new_s.append(str(s[i]))

		s = new_s
	
	return ''.join(s)


n = 6
print("{}th term:	{}".format(n, look_and_say(n)))