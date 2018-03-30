#school model with 
import random
import sys

class School:
    def __init__(self, name):
        self.schoolName = name
        self.students = []  #list of student IDs
        self.teachers = []
        self.classList = []
        self.programs = []
        self.enrollment = 0
        self.staffCount = 0
        self.programCount = 0
        self.budget = 0
        self.classBudg=[]
        self.teachBudg=[]
        self.progBudg=[]
        self.classBudgRat = 0.20 #what percent of the budget classes receive
        self.teachBudgRat = 0.50
        self.progBudgRat = 0.30 #ratio
    def getBudg(self):
        return self.budget
    def enroll(self, sID): #enroll student in school
        self.students.append(sID)
        self.enrollment += 1
    def hireStaff(self, teacherLast):
        self.teachers.append(teacherLast)
        self.staffCount +=1    
    def expel(self, sId): #unenroll a student from school based on student ID
        self.students.remove(sId)
        self.enrollment-=1
    def fire(self, teacherLast):
        self.teachers.remove(teacherLast)
        self.staffCount-=1
    def addClass(self, class1):
        self.classList.append(class1.getCId())
    def addProgram(self, program):
        self.programs.append(program)
        self.programCount+=1
    def cutProgram(self, program):
        self.programs.remove(program)
    def printStudents(self):
        print self.students
    def printTeachers(self):
        for i in range(0,len(self.teachers)):
            print self.teachers[i].getLastTName()
    def printPrograms(self):
        print self.programs
        
    def createBudget(self, budg):
        self.budget = budg
        print ("For a $",self.budget," budget:")
        acb=float((self.classBudgRat*self.budget))/ len(self.classList)#avg class budget
        print ("Average Class Budget is " , acb)
        for i in range (0,len(self.classList)):
            self.classBudg.append((self.classList[i], acb))
        atb = float(self.teachBudgRat*self.budget) / len(self.teachers)
        print("Average Teacher Salary is ", atb)
        for i in range (0,len(self.teachers)):
            self.teachBudg.append((self.teachers[i].getLastTName(), atb))
        apb = float(self.progBudgRat*self.budget)/len(self.programs)
        print ("Average Program Budget is ", apb)
        for i in range (0,len(self.programs)):
            self.progBudg.append((self.programs[i], apb))
    def newRatio(self):
        self.classBudgRat = float(input("Enter ratio for Class Budget"))
        self.teachBudgRat = float(input("Enter ratio for Teacher Budget"))
        self.progBudgRat = float(input("Enter ratio for Program Budget"))
        if classBudgRat + teachBudgRat + progBudgRat ==1.0:
            createBudget(self, budg) #redistribute budget
        else:
            print "Not a valid budget ratio. Try again"
            newRatio(self)

 
                           

class Student:    
    def __init__(self, f, l, y):
        self.sId = random.randint(100, 1000) #create random student ID
        self.firstName = f
        self.lastName = l
        self.classYear = y
        self.classesEnrolled = []
        
    def changeYear(self, newYear): #change student class year
        self.classYr = newYear
    def getFName(self):
        return self.firstName
    def getLName(self):
        return self.lastName       
    def getSId(self):
        return self.sId 
    def getYr(self):
        return self.classYr

class Course:
    def __init__(self, n, t):
        self.cId = random.randint(10,100)#create random course number
        self.courseName = n
        self.time = t #time class meets
        self.roster = [] #list of students in class

    def getCId(self):
        return self.cId
    def getTime(self):
        return self.time
    def getCName(self):
        return self.courseName
    def changeTime(self, newTime):
        self.time = newTime
    def changeName(self,newName):
        self.courseName = newName
    def alphabetize(self, roster):
        for i in range (0, len(roster)): #merge sort to alphabetize
              self.roster.sort()      

class Teacher:
    def __init__(self, sal, last):
        self.salutation = sal
        self.lastTName = last
        self.classesTaught=[]
    def getLastTName(self):
        return self.lastTName
    def addClassTaught(self, class2):
        self.classesTaught.append(class2)
    def deleteClassTaught(self, class2):
        self.classesTaught.remove(class2)

class Program:
    def __init__(self, name):
        self.pName = name  #program name
    def getPName(self, pname):
        return self.pName

def main():
    school1 = School('American High School')
    student1=Student('Jane','Doe',2018)
    student2=Student('John','Doe', 2019)
    student3 = Student('George','Washington',2020)
    school1.enroll(student1.getSId())
    school1.enroll(student2.getSId())
    school1.enroll(student3.getSId())
    teacher1 = Teacher('Mr.','Johnson')
    teacher2=Teacher('Mrs.', 'Knowles')
    school1.hireStaff(teacher1)
    school1.hireStaff(teacher2)
    biology = Course('Biology','1:00')
    school1.addClass(biology)
    usHist = Course('U.S. History','9:00')
    music = Program('Orchestra')
    drama = Program('Drama Club')
    football = Program('Football')
    school1.addClass(usHist)
    school1.addProgram(music)
    school1.addProgram(drama)
    school1.addProgram(football)
    school1.printStudents()
    school1.printTeachers()
    school1.createBudget(1000)
  
    
    
    


        
