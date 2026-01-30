#InstamethodEx.py
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print("Hi",self.name)
        print("Your Marks :",self.marks)
    def grade(self):
        if self.marks>=60:
            print("You Got a First Grade")
        elif self.marks>=50:
            print("You Got a Second Grade")
        elif self.marks>=35:
            print("You Got a Third Grade")
        else:
            print("Your Failed")
n = int(input("Enter for number of students :"))
for i in range(n):
    name = input("Enter Student Name :")
    marks = int(input("Enter Student Marks :"))
    s = student(name,marks)
    s.display()
    s.grade()
    print("="*50)