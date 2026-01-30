#Program for Demonstrating the Need of Iterators
#DictIterEx.py
x={10:"Python",20:"C",30:"Java",40:"C++"}
print("Type of x=",type(x)) # <class, dict>
print(x)
itr=iter(x)
print("Type of itr=",type(itr)) # <class 'dict_key_iterator'>
print("---------------------------------------")
print("Content of Dict_Iterator")
print("---------------------------------------")
for val in itr:
	print("{}\t{}".format(val,x.get(val)))
print("---------------------------------------")

