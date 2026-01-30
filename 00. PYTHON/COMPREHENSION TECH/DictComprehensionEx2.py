#Program for accepting List of words and find their length
#DictComprehensionEx1.py
print("Enter List of Words separated by comma:")
wordslengths={word:len(word) for word in input().split(",")}
for w,l in wordslengths.items():
    print("\t{}--->{}".format(w,l))
print("---------------------OR----------------------------")
print("Enter List of Words separated by comma:")
for w,l in {word:len(word) for word in input().split(",")}.items():
    print("\t{}--->{}".format(w,l))
