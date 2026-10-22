class Student:
    count=0 
 #it will restrict the creation of new attribute in class Student
    department="CSE"

    def __init__(self, first, last, rollNO):
        self.first = first
        self.last = last
        self.rollNO = rollNO
        self.email = f"{rollNO}@cutmap.ac.in"
        Student.count += 1
    #creating a method to display full name of student
   
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def department1(self):
        return self.department

std1=Student("Hari","prasad",231801370055)
std2=Student("sanjay","sahu",231801370018)
std3=Student("vinay","kumar",231801370022)

std2.first="Sanjay"
std1.rollN0=231801370056  #typo


print(std1.__dict__)#it not changing the value of rollNO because of typo in rollN0
std1.department="CSE" #it will create a new attribute department in class Student
print(std2.__dict__)
print(std3.__dict__)
print(std1.fullname())
print(Student.count)
print(std1.department) #it will print the value of department attribute of std1 object
for std in Student:
    print(std.department) #it will give error because std2 and std3 object does not have department attribute
    
print(Student.__dict__)