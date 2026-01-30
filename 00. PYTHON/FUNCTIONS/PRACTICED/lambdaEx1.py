list1= ["Mahesh","Suresh","Manikanta","Sunil","Mahesh","Raghavendra","Vishnu","Ajay"]

list1=list(set(list1))
Starting_Letter_Set = set();
for val in list1:
    #adding all starting letters in Set
    Starting_Letter_Set.add(val[0])

Starting_Letter_Set = list(Starting_Letter_Set)
print(Starting_Letter_Set)
for i in range(len(Starting_Letter_Set)):
    newList = list();
    for val in list1:
         if(Starting_Letter_Set[i]==val[0]):
             newList.append(val)
    else:
        print("List Of Names Starting with {} are {}".format(Starting_Letter_Set[i],newList))

