#bankproOops.py
class customer:
    bankname = "SBI"
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amt):
        self.balance = self.balance+amt
        print('Balance After Deposit :',self.balance)
    def withdraw(self,amt):
        if self.balance<amt:
            print("InSufficient Funds..,Can't perform this Operation")
            #sys.exit()
        self.balance = self.balance-amt
        print("Balance After Withdraw :",self.balance)

# Main Program
name = input("Enter Your Name :")
c = customer(name)
print("="*50)
print("\t\t\tWel Come To ",customer.bankname)
print("="*50)
print(" d.deposit")
print(" w.withdraw")
print(" e.exit")
print("="*50)
while True:
    option = input('Enter ur option:').lower()
    if option=="d":
        amt = float(input("Enter the Amount for Deposit :"))
        c.deposit(amt)
    if option=="w":
        amt = float(input("Enter the Amount for withdraw :"))
        c.withdraw(amt)
    if option=="e":
        print("Thank you Visit Again")
        sys.exit()
    else:
        print("Please Enter Valid Option ")
    print("*"*50)