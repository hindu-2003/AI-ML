#Program for Demonstrating Data Encapsulation
#CurrentAccountEx1.py
class Account:
    def __getaccdet(self):
        self.acno=999
        self.cname="Rossum"
        self.bal=5.6
        self.pin=7867
        self.bname="SBI"
    def getAcInfo(self):
        self.__getaccdet()
        print("Account Number=",ac.acno)
        print("Account Holder Name=", ac.cname)
        print("Account Balance=",ac.bal)
        print("Account PIN=",ac.pin)
        print("Account Branch Name=", ac.bname)


#Main Program
ac=Account()
ac.getAcInfo()
