def employee(first,last,pay):
    email=f"{first}.{last}@company.com"
    return {"first": first, "last": last, "email": email, "pay": pay,}

def salary(emp,percent):
    emp["pay"] = int(emp["pay"] * (1 + percent / 100))
    return emp



emp_1=employee("John","Doe",50000)

print(emp_1)
salary(emp_1,4)
print(emp_1)
