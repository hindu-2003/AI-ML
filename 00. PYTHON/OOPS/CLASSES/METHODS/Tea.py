#Tea.py<---File Name and Module Name
class Teacher:
    def readteacherdata(self):
        print('-'*50)
        self.tno = int(input("\tEnter Teacher Number:"))
        self.tname = input("\tEnter Teacher Name:")
        self.subject = input("\tEnter Teacher Subject:")
        self.exp=float(input("\tEnter Teacher Experience:"))