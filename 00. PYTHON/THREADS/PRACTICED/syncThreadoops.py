#syncThreadoops.py
import threading,time
class oop:
    @staticmethod
    def multitable(n):
        L.acquire()
        if n<=0:
            print(" '{}'  is a Invalid input".format(n))
        else:
            print("------------------------------------------------")
            print("{} --->Mul table for :{}".format(threading.current_thread().name,n))
            print("------------------------------------------------")
            for i in range(1,11):
                print("\t{} x {} = {}".format(n,i,n*i))
                time.sleep(0.00625)

        L.release()
L = threading.Lock()
# Main Program
t1=threading.Thread(target=oop().multitable,args=(20,))
t2=threading.Thread(target=oop().multitable,args=(-19,))
t3=threading.Thread(target=oop().multitable,args=(18,))
t4=threading.Thread(target=oop().multitable,args=(15,))
t5=threading.Thread(target=oop().multitable,args=(-18,))
t6=threading.Thread(target=oop().multitable,args=(17,))
#Dispatch the objects
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
