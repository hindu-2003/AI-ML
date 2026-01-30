#NameValidation.py
while(True):
    urname=input("Enter Ur Name:").strip() # urname=Guido Van Ro4ssum
    if(len(urname)==0):
        print("\tDon't enter space for Name--try again")
    else:
        #validation Code for name
        words=urname.split()  # ['Guido', 'Va$n', 'Ro4ssum']
        res="valid"
        for word in words:
            if( not word.isalpha()):
                res="invalid"
                break
        if(res=="invalid"):
            print("{} is Invalid Name--try again".format(urname))
        elif(res=="valid"):
            print("{} is Valid Name".format(urname))
            break
