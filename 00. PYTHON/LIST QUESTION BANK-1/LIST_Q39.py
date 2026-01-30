#LIST_Q39.PY
# Write a Python program to convert a list of multiple integers into a single integer.
# 		Sample list: [11, 33, 50]
# 		Expected Output: 113350
lst = [11, 33, 50]
res = [str(val) for val in lst]
print("List items are clubbed")
print("".join(res))


