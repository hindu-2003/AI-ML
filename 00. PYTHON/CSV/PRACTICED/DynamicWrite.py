import csv
try:
    noc = int(input("How many columns you want :"))
    if noc<=0:
        print("{} is invalid input".format(noc))
    else:
        hname = []
        for i in range(1,noc+1):
            val= input("Enter {} value for columns: ".format(i))
            hname.append(val)
        else:
            nor = int(input("How many columns you want :"))
            if nor<=0:
                print("{} is invalid input".format(nor))
            else:
                records = []
                for i in range(1,nor+1):
                    print("="*50)
                    print("Enter the {} Record details :".format(i))
                    print("=" * 50)
                    record = []
                    for val in hname:
                        rc = input("Enter the {} value :".format(val))
                        record.append(rc)
                    records.append(record)
                print("*"*50)
        while(1):
            filename = input("Enter the file name with Extension of __.csv format only : ")
            if filename.endswith(".csv"):
                with open(filename,"a")as fp:
                    obj=csv.writer(fp)
                    obj.writerow(hname)
                    obj.writerows(records)
                    print("{} succesfully created csv file ".format(filename))
                    break
            print("\t\tPlease Enter the file name with Extension of __.csv (EX: Python.csv) ")
except ValueError:
    print("dont Enter the alnums,strs,symbols and only numbers allowed")