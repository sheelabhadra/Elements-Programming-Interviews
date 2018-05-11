def str_to_int(s):
	res = 0
	if s[0] == '-':
		for i in range(1,len(s)):
			res = 10*res + (ord(s[i]) - ord('0'))
		return -res
	
	else:
		for i in range(len(s)):
			res = 10*res + (ord(s[i]) - ord('0'))
		return res

s = '-123'
print(str_to_int(s))