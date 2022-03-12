class Employee:    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def get_employee_details(self):
        newStr = f"name: {self.name}\tsalary: {self.salary}"
        return newStr

emp01 = Employee("bob",12345)
emp02 = Employee("john",2000)

print(emp01.get_employee_details())
print(emp02.get_employee_details())
