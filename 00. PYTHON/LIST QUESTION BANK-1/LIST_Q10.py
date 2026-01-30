#Write a Python program to find the list of words that are longer than n from a given list of words.
#LIST_Q10.py
n =int(input("Enter the number for how many values in list :"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    words = []
    val = 1
    n_above = []
    for i in range(1,n+1):
        val = input("Enter the {} value:".format(i))
        l = len(val)
        if  (l>n):
            n_above.append(val)

      #  n_above.append(abv)
        words.append(val)
    print("-" * 50)
    print("list is created{}:".format(words))
    print("-"*50)
    print("Length of {} letters above words :{}".format(n,n_above))
    print("*" * 50)