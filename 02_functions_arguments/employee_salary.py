"""Create an employee record and apply a salary increase."""


def create_employee(first, last, pay):
    email = f"{first.lower()}.{last.lower()}@company.com"
    return {"first": first, "last": last, "email": email, "pay": pay}


def increase_salary(employee, percent):
    if percent < 0:
        raise ValueError("percent must be zero or greater")
    employee["pay"] = int(employee["pay"] * (1 + percent / 100))
    return employee


if __name__ == "__main__":
    employee = create_employee("John", "Doe", 50000)
    print(employee)
    increase_salary(employee, 4)
    print(employee)
