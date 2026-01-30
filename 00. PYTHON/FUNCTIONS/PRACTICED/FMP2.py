text = "str2li74ng6"
digs=list(filter(lambda ch: ch.isdigit(),text))
alpha=list(filter(lambda ch: ch.isalpha(),text))
digs.sort()
alpha.sort()
print("="*50)
print("Sorted alpha ",alpha)
print("Sorted digits ",digs)
print("_"*50)
even=[(val) for val in digs if int(val)%2==0]
odd=[(val) for val in digs if int(val)%2==1]
print("Even numbers in Text",even)
print("_"*50)
print("Odd numbers in Text",odd)
print("*"*50)


