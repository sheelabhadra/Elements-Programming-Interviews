# Evaluate an arithmetic expression written in Reverse Polish Notation (RPN)

# Approach: Use a stack to store intermediate results. Whenever we encounter
# a number, we push it to the stack. Whenever we encounter an operator, we
# pop the top 2 elements in the stack, evluate the result and push it to the stack.

def evalRPN(s):
	operators = set(['+','-','x','/'])
	tokens = s.split(',')

	stack = []
	for t in tokens:
		if t not in operators:
			stack.append(int(t))
		else:
			b = stack.pop()
			a = stack.pop()
			if t == '+':
				stack.append(a+b)
			elif t == '-':
				stack.append(a-b)
			elif t == 'x':
				stack.append(a*b)
			else:
				stack.append(int(a/b))
		print(stack)
	return stack.pop()

s = "3,4,+,2,x,1,+"
res = evalRPN(s)
print("RPN expression: {}".format(s))
print("After evaluation: {}".format(res))





