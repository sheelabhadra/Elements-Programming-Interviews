""" PROBLEM
	Compute all mneumonics for a phone number

	WAP which takes as input a phone number, specified as a string of digits, and returns
	all possible character sequences that correspond to the phone number. 

"""

""" SOLUTION
	Using recursion instead of writing nested loops.

"""

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'YUV', 'WXYV')

def phone_mneumonic(number):
	def helper(digit):
		if digit == len(number):
			mneumonics.append(''.join(partial_mneumonic))
		else:
			# try all possible characters for this digit
			for c in MAPPING[int(number[digit])]:
				partial_mneumonic[digit] = c
				helper(digit+1)

	mneumonics, partial_mneumonic = [], [0]*len(number)
	helper(0)
	return mneumonics


number = "23"
print("The mneumonic for the number {} is {}".format(number, phone_mneumonic(number)))
