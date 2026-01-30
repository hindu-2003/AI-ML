#Program for finding length of Every word of Line of Text by using functions
#WordsLengthFunctions1.py
import sys
def findwordslength(line):

    if(len(line.strip())==0):
        print("U must enter a line of Text:")
    elif(line.isdigit()):
        print("U must enter a Line of Text but not Digits")
    else:
        words=line.split()
        print("-"*50)
        print("-" * 50)
        for word in words:
            print("\t{}--->{}".format(word,len(word)))
        print("-" * 50)
        sys.exit()

#Main Program
while(True):
    line=input("Enter Line of Text:")
    findwordslength(line) # Function Call