# Find the GCD of 2 numbers

## SOLUTION: Key idea is that if y > x, GCD(x,y) = GCD(x,y-x)
# This can also be acheived using the mod (%) operator

def find_gcd(x,y):
	if y == 0:
		return x
	else:
		return find_gcd(y, x%y)

x, y = 36, 156
print("GCD of {} and {}: {}".format(x,y,find_gcd(x,y)))