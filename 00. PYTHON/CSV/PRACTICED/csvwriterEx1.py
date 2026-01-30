import csv
col = ["SNO","NAME","MARKS"]
rows = [[10,"MB",66],
        [20,"AB",99],
        [30,"RR",88]]
with open("stud.csv","w",newline="")as fp:
    cs = csv.writer(fp)
    cs.writerow(col)
    cs.writerows(rows)
    print("Execution successful")
