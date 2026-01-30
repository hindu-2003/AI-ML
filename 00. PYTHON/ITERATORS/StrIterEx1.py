#Program for Demonstrating the Need of Iterators
#StrIterEx1.py
x=123445
print("Type of x=",type(x)) # <class, str>
print(x)
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'str_ASCII_iterator'>
print("---------------------------------------")
print("Content of Str_Iterator")
print("---------------------------------------")
for val in itr:
	print(val)
print("---------------------------------------")

