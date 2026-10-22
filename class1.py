class library:
    def __init__(self,name,roll_no,purpose,in_time,out_time):
        self.name=name
        self.roll_no=roll_no
        self.purpose=purpose
        self.in_time=in_time
        self.out_time=out_time  

    def reading(self,name):
        if self.name == name and self.purpose == "reading":
            print("Name:",self.name)
            print("Roll No:",self.roll_no)
            print("Purpose:",self.purpose)
            print("In Time:",self.in_time)
            print("Out Time:",self.out_time)

std1=library("sneha", 1, "reading", "10:00", "11:00")
std1.reading("sneha")