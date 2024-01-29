class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee(self):
        print(f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}")


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_table(self, sort_parameter):
        if sort_parameter == 1:  # Sort by Age
            self.employees.sort(key=lambda x: x.age)
        elif sort_parameter == 2:  # Sort by Name
            self.employees.sort(key=lambda x: x.name)
        elif sort_parameter == 3:  # Sort by Salary
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        for emp in self.employees:
            emp.display_employee()


# Creating employee objects
employee1 = Employee("161E90", "Ramu", 35, 59000)
employee2 = Employee("171E22", "Tejas", 30, 82100)
employee3 = Employee("171G55", "Abhi", 25, 100000)
employee4 = Employee("152K46", "Jaya", 32, 85000)

# Creating employee table object
employee_table = EmployeeTable([employee1, employee2, employee3, employee4])

# User input for sorting parameter
sort_option = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
employee_table.sort_table(sort_option)

# Displaying sorted table
employee_table.display_table()
