d = int(input("Enter a Digit:"))
if (d==0):
    print("{} is ZERO".format(d))
else:
    if (d == 1):
        print("{} is ONE".format(d))
    else:
        if (d == 2):
            print("{} is ZERO".format(d))
        else:
            if (d == 3):
                print("{} is THREE".format(d))
            else:
                if (d == 4 ):
                    print("{} is FOUR".format(d))
                else:
                    if (d == 5):
                        print("{} is FIVE".format(d))
                    else:
                        if (d == 6):
                            print("{} is SIX".format(d))
                        else:
                            if (d == 7):
                                print("{} is SEVEN".format(d))
                            else:
                                if (d == 8):
                                    print("{} is EIGHT".format(d))
                                else:
                                    if (d == 9):
                                        print("{} is NINE".format(d))
                                    else:
                                        if d<0 and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                            print("{} is negative number".format(d))
                                        else:
                                            if d<0 and d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                                print("{} is negative digit".format(d))
                                            else:
                                                if d>0 and d not in [1,2,3,4,5,6,7,8,9]:
                                                    print("{} is positive number".format(d))

print("Execution is completed")