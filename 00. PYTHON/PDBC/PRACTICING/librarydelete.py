import oracledb as orc
def deletebook():
    while(10):
        con = orc.connect("system/mahesh@localhost/xe")
        cur = con.cursor()
        bookno = int(input("Enter book number for deleting :"))
        dq =("delete from library where bno = %d "%(bookno))
        ex = cur.execute(dq)
        con.commit()
        if cur.rowcount>0:
            print("{} is deleted from library".format(cur.rowcount))
        else:
            print("{}number in oracle data base".format(bookno))
        ch = (input("You want to delete another book (yes/no): "))
        if ch.lower() == "no":
            print("Thanks for using this program")
            break

