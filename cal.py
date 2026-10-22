class calculator:
    def __init__(self , a , b):
        self.a = a
        self.b = b
    def add(self):
        return f"{self.a} + {self.b} = {self.a + self.b}"
    def subtract(self):
        return f"{self.a} - {self.b} = {self.a - self.b}"
    def multiply(self):
        return f"{self.a} * {self.b} = {self.a * self.b}"
    def divide(self):
        if self.b != 0:
            return f"{self.a} / {self.b} = {self.a / self.b}"
        else:
            return "Error: Division by zero"
    def table(self):
        for i in range(1, 11):
            print(f"{self.a} * {i} = {self.a * i}")
            pass
           
    
cal1=calculator(10, 5)
print(cal1.add())
print(cal1.subtract())
print(cal1.multiply())
print(cal1.divide())
print(cal1.table())
