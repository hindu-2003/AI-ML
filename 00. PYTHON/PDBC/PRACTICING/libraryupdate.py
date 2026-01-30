import oracledb as orc
def updatebook():
    while(1):
        try:
            con = orc.connect("system/mahesh@localhost/xe")
            cur = con.cursor()
            bookno = int(input("Enter the book number for updating datails :"))
            pri = float(input("Enter the new price :"))
            pub = input("Enter the new publishers of book :")
            uq = "update library set price=%f,PUBLICTION='%s' where bno=%d"
            cur.execute(uq % (pri,pub,bookno))
            con.commit()
            print()
            if cur.rowcount>0:
                print("{} book is updated".format(cur.rowcount))
            else:
                print("{} number is does't Exist in this library")
            ch = input(" You want update another book details (yes/no):")
            if ch.lower() == "no":
                print('Thanks for using this program')
                break
        except orc.DatabaseError as db:
            print("\tproblem in data base",db)
        except ValueError as va:
            print("\tDont enter alphanums and symbols and strs",va)



