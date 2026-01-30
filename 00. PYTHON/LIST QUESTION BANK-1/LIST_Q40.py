#LIST_Q40.py
#Write a Python program to split a list based on first character of word
class split:
    def split(self,lst):
        self.d = {}
        for i in lst:
            first = i[0]
            self.d[first] = i
        print(self.d)
# Main Program
list = [val for val in input("Enter str's for List separates with space :").split()]
c = split()
c.split(list)