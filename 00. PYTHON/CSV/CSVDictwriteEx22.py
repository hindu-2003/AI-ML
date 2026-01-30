#CSVdynamicEx2.py
import csv
try:
	noc = int(input("Enter How Many Columns You Want:"))
	if (noc<=0):
		print("Invalid Input For Heading of Columns")
	else:
		hname=[]
		for i in range(1,noc+1):
			name=input("Enter {} Heading name:".format(i))
			hname.append(name)
		else:
			nor = int(input("Enter How Many Rows You Want:"))
			if(nor<=0):
				print("Invalid Input For Rows Of Records")
			else:
				records = []
				for i in range(1,nor+1):
					print("="*50)
					print("Enter {} Records:".format(i))
					print("="*50)
					record ={}
					for name in hname:
						val = input("Enter {} value:".format(name))
						record[colname]=val
					records.append(record)
	while("kvr"):
		filename=input("Enter The file Name with Extension of .csv :")
		if filename.endswith(".csv"):
			with open("D:\\My\\PY\\PSF\\CSV\\"+filename,"w",newline="") as fp:
				csvw = csv.writer(fp)
				csvw.writerow(hname)
				csvw.writerows(records)
				print("CSV file created Dynamically-----verify")
				break
		else:
			print("Please Must Enter Extension has been .csv format only (EX: data.csv)")
except ValueError:
	print("	Don't Enter Alphabets,Alphanums,symbols")



							
						
					
					

	
	
	
	