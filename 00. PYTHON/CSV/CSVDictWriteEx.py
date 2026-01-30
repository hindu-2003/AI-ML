#Program for Creating CSV File bY using Dict Data
#CSVDictWriteEx.py
import csv # Step-1
hnames=["ENO","NAME","SAL"] # Step-2
records=[{"ENO":100,"NAME":"RS","SAL":4.5},
        {"ENO":110,"NAME":"TR","SAL":6.5},
        {"ENO":120,"NAME":"DR","SAL":2.5},
        {"ENO":140,"NAME":"ST","SAL":2.6},
        {"ENO":160,"NAME":"KV","SAL":0.0}] # Step-3
#Choose the CSV File and Open in Write Mode
with open("employee.csv","w") as fp: # Step-4
        csvdwr=csv.DictWriter(fp,fieldnames=hnames)  # Step-5
        csvdwr.writeheader() # Step-6
        csvdwr.writerows(records) # Step-7
        print("CSV File Created--Verify")
