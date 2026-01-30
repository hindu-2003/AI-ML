#Program for Demonstrating Data Encapsulation
#CurrentAccountEx2.py
class Account:
    def __init__(self):
        self.__acno=999
        self.cname="Rossum"
        self.__bal=5.6
        self.__pin=7867
        self.bname="SBI"
    def getAcInfo(self):
        print("Account Number=", self.__acno)
        print("Account Holder Name=", self.cname)
        print("Account Balance=", self.__bal)
        print("Account PIN=", self.__pin)
        print("Account Branch Name=", ac.bname)

#Main Program
ac=Account()
ac.getAcInfo()

