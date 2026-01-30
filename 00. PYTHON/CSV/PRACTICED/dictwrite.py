import csv

hname = ["eno","name","sal"]
row = [{"eno":10,"name":"MB","sal":100},
       {"eno":20,"name":"AB","sal":200},
       {"eno":30,"name":"MM","sal":300}]
with open("emp.csv","w") as fp:
    csvd = csv.DictWriter(fp,fieldnames=hname)
    csvd.writeheader() #self
    csvd.writerows(row)