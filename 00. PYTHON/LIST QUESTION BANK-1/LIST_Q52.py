#52. Write a Python program to compute the difference between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# 	Color1-Color2: ['white', 'orange', 'red']
# 	Color2-Color1: ['black', 'yellow']
color1= ["red", "orange", "green", "blue", "white"]
color2= ["black", "yellow", "green", "blue"]
ls1 = set(color1)
ls2 = set(color2)
diff1 = ls1-ls2
diff2 = ls2-ls1
print(list(diff1))
print(list(diff2))