""" PROBLEM
	Multiply two arbitrary precision integers

	WAP that takes two arrays representing integers, and returns their representing an integer.

"""

""" SOLUTION


"""

def multiply(num1, num2):
	if (num1[0] < 0) or (num2[0] < 0):
		sign = -1
	else:
		sign = 1
	num1[0], num2[0] = abs(num1[0]), abs(num2[0])

	res = [0]*(len(num1) + len(num2))
	for i in reversed(range(len(num1))):
		for j in reversed(range(len(num2))):
			res[i + j + 1] += num1[i]*num2[j]
			res[i + j] += res[i + j + 1]//10
			res[i + j + 1] %= 10

	# Remove leading zeroes
	for i in range(len(res)):
		if res[i] != 0:
			break

	ans = res[i:]
	return [ans[0]*sign] + ans[1:]


a = [1,9,3,7,0,7,7,2,1]
b = [-7,6,1,8,3,8,2,5,7,2,8,7]

print("Product of {} and \n{} is \n{}".format(a,b,multiply(a,b)))
