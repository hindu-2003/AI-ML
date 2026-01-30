#SharesDemo.py--Viewer Program
import Shares,time,importlib
def dispshares(d):
    print("-"*50)
    print("\tShareName\tShareValue")
    print("-" * 50)
    for sn,sv in d.items():
        print("\t{}\t\t\t{}".format(sn,sv))
    print("-" * 50)

#Main Program
d=Shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 20 Seconds")
time.sleep(20)
print("I am coming-out-off sleep after 20 Seconds")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 20 Seconds")
time.sleep(20)
print("I am coming-out-off sleep after 20 Seconds")
importlib.reload(Shares)
d=Shares.sharesinfo()
dispshares(d)