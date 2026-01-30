import pickle
with open("Emp.txt","ab")as f:
    while(3):
        empno = int(input("Enter a emp no :"))
        ename = input("Enter Employee name: ")
        sal = float(input("Enter Salary: "))
        lst = []
        lst.append(empno)
        lst.append(ename)
        lst.append(sal)
        pickle.dump(lst,f)
        choice = input("Do you want one more list yes/no :")
        if choice.lower()=="no":
         break

