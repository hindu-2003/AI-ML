import oracledb as orc
def addbook():
    while(10):
        con = orc.connect("system/mahesh@localhost/xe")
        cur = con.cursor()
        bno = int(input("Enter the Book Number:"))
        bname = input("Enter the book name :")
        price = float(input("Enter the book price :"))
        pub = input("Enter the book publication :")
        iq = ("insert into library values(%d,'%s',%f,'%s')" %(bno, bname,price,pub))
        ex = cur.execute(iq)
        con.commit()
        print("Execution complete successfully")
        ch = input("One more book u want to add library (yes/no) :")
        if ch.lower() == "no":
            print("Thanks for using this program")
            break

