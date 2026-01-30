#Program for geenrating Mul table for a given Number by using functions
#MultableFunEx1.py
def  multable(n):
    if(n<=0):
        print("{} is Invalid Input".format(n))
    else:
        print("-"*50)
        print("Mul Table for :{}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t{} x {} = {}".format(n,i,n*i))
        print("-" * 50)
#Main Program
multable(int(input("Enter a Number for generating Mul table:"))) # Function Call

