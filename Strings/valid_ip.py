# WAP that determines where to add periods to a decimal string so that 
# the resulting string is a valid IP address. There may be more than one
# valid IP address corresponding to a string in which case you should 
# print all possibilities.

def is_valid_ip(s):
	def valid_part(s):
		# '0' is valid, '0x', '00x' and > '255'are invalid
		return len(s) == 1 or (s[0] != '0' and int(s) < 255)

	res, parts = [], [None]*4

	for i in range(1, min(len(s), 4)):
		parts[0] = s[:i]
		if valid_part(parts[0]):
			for j in range(1, min(len(s)-i, 4)):
				parts[1] = s[i:i+j]
				if valid_part(parts[1]):
					for k in range(1, min(len(s)-i-j, 4)):
						parts[2] = s[i+j:i+j+k]
						parts[3] = s[i+j+k:]
						if valid_part(parts[2]) and valid_part(parts[3]):
							res.append('.'.join(parts))

	return res


s = '19216811'
print("Given string:	{}\nValid IP(s):	{}".format(s,is_valid_ip(s)))

