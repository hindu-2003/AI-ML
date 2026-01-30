lst = 	[1, 1, 2, 3, 4, 4, 5, 1]
res = 	[1, 1, 12, 2, 3, 4, 4, 5, 1]

# finding num values
l = set(res)-set(lst)
num = l.pop()

# demonstrting problem
def add(p):
    p.insert(2, num)
    return p
print('*'*50)
op = add(lst)
if op == res:
	print("\tEXECUTION PERFECTLY COMPLETED")
	print('='*50)
	print(op)
	print('*'*50)
