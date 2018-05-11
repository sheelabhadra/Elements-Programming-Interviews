def int_to_str(x):
	isNegative = False

	if x < 0:
		isNegative = True
		x = abs(x)
	
	s = []
	while x > 0:
		d = chr(ord('0') + x%10)
		s.append(d)
		x = x//10;

	if isNegative:
		return '-' + ''.join(s[::-1])

x = -123
print(int_to_str(x))
