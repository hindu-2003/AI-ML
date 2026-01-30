#=>Accept the List Salary Values within the Range of 0 to 1000 (Neg Values and More than 1000 not allowed)
#=>Obtain List of Salaries ranges from 0 to 500
#=>Obtain List of Salaries ranges from 501 to 1000
#=>Give 10% Hike those employes whose Sal ranges from 0 to 500
#=>Give 20% Hike those employes whose Sal ranges from 501 to 1000
#=>Find the Total Salary of employees whose salary ranges from 0 to 500 before and after hike
#=>Find the Total Salary of employees whose salary ranges from 501 to1000 before and after hike
#FilterMapReduceEx.py
import functools
def filtermapreduce():
    print("Enter List of Salaries ranges from 0 to 1000:")
    oldsals=[float(sal) for sal in input().split() if 0<=float(sal)<=1000]
    print("Given Salaries")
    print(oldsals) # [0.0, 1000.0, 500.0, 501.0, 750.0]
    #Filter the salaries ranges from 0 to 500
    sal0_500=list(filter(lambda sal:0<=sal<=500,oldsals))
    # Filter the salaries ranges from 501 to 1000
    sal501_1000 = list(filter(lambda sal: 501<= sal <= 1000,oldsals))
    #Give 10% Hike those employes whose Sal ranges from 0 to 500
    hikesal0_500=list(map(lambda sal:sal+sal*10/100,sal0_500))
    # Give 20% Hike those employes whose Sal ranges from 501 to 1000
    hikesal501_1000 = list(map(lambda sal: sal + sal * 20 / 100, sal501_1000))
    print("------------------------------------------------------")
    print("\t\tSal0-500\t\tHike Sal0-500")
    print("------------------------------------------------------")
    for sal1,sal2 in zip(sal0_500,hikesal0_500):
        print("\t\t{}\t\t{}".format(sal1,sal2))
    #Find the Total Salary of employees whose salary ranges from 0 to 500 before and after hike
    totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500) # Before Hike
    tothikesal0_500 = functools.reduce(lambda sal1, sal2: sal1 + sal2, hikesal0_500)# after Hike
    print("------------------------------------------------------")
    print("\tTotal:{}\t\tTotal:{}".format(totsal0_500,tothikesal0_500))
    print("------------------------------------------------------")
    print("*"*60)
    print("\t\tSal501-1000\t\tHike Sal501-1000")
    print("------------------------------------------------------")
    for sal1, sal2 in zip(sal501_1000, hikesal501_1000):
        print("\t\t{}\t\t{}".format(sal1, sal2))
    print("------------------------------------------------------")
    # Find the Total Salary of employees whose salary ranges from 501 to 1000 before and after hike
    totsal501_1000 = functools.reduce(lambda sal1, sal2: sal1 + sal2, sal501_1000)  # Before Hike
    tothikesal501_1000 = functools.reduce(lambda sal1, sal2: sal1 + sal2, hikesal501_1000)  # after Hike
    print("\tTotal:{}\t\tTotal:{}".format(totsal501_1000, tothikesal501_1000))
    print("="*60)
    totoldsal=totsal0_500+totsal501_1000
    totnewsal=tothikesal0_500+tothikesal501_1000
    print("TOTAL OLD SALS={}\t TOTAL NEW SALS={}".format(totoldsal,totnewsal))
    print("=" * 60)

#Main Program
filtermapreduce()# Function Call

