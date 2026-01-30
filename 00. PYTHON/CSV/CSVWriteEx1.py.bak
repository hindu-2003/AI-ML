#Program for creating CSV File though Python Lang.
#CSVWriteEx1.py
import csv # Step-1
hname=["EMPNO","NAME","SAL"] # Step-2
records=[ [100,"Rossum",4.5],
				[200,"Travis",5.6],
				[300,"Dennis",3.4],
				[400,"Strup",4.5],
				[500,"Ritche",6.7] ] # Step-3---List in List--called Nested List
#Choose the CSV File and Open it into write Mode---Step-4
with open("E:\\KVR-PYTHON-6PM\\CSV\\NOTES\\emp.csv","w") as fp:
	csvwr=csv.writer(fp) # Step-5---here csvwr is an object of <class,csv.writer>
	#write the Header Names---
	csvwr.writerow(hname) # Step-6
	#Write the Records 
	csvwr.writerows(records) # Step-7
	print("CSV File Created Dynamically through Code--verify")
