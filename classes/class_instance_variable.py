class Employee:
    name = "ACME"
    def __init__(self,name):
        self.name = name

employee_instance01 = Employee("A")
employee_instance02 = Employee("B")
employee_instance03 = Employee("C")

print(Employee.name)
print(employee_instance01.name)
print(employee_instance02.name)
print(employee_instance03.name)